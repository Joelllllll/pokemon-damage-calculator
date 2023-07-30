import os
import sys
from dataclasses import dataclass

from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from app.main import app
from app.db.models.pokemon import Pokemon, EVs, IVs, PokemonStats


# easy testing https://fastapi.tiangolo.com/tutorial/testing/
client = TestClient(app)


@dataclass
class TestPayload:
    pokemon: Pokemon
    evs: EVs
    ivs: IVs
    level: int = 100
    move_name: str = None


PIKACHU = TestPayload(**{
    "pokemon": {
        "total": 320,
        "pokemon_number": 25,
        "type_1": "Electric",
        "attack": 55,
        "sp_atk": 50,
        "speed": 90,
        "legendary": False,
        "pokemon_name": "Pikachu",
        "type_2": None,
        "hp": 35,
        "defense": 40,
        "sp_def": 50,
        "generation": 1,
    },
    "evs": {
        "hp": 100,
        "attack": 0,
        "defense": 0,
        "special_attack": 0,
        "special_defense": 0,
        "speed": 0,
    },
    "ivs": {
        "hp": 0,
        "attack": 31,
        "defense": 0,
        "special_attack": 0,
        "special_defense": 0,
        "speed": 0,
    },
    "level": 100,
    "move_name": None,
})


class TestAPI:
    def test_get_pokemon(self):
        res = client.get(
            f"/pokemon/pikachu", json={"evs": PIKACHU.evs, "ivs": PIKACHU.ivs}
        )
        assert res.status_code == 200
        assert res.json() == PIKACHU.__dict__

    def test_battle(self):
        res = client.post(
            f"/battle",
            json={
                "attacking": {
                    "pokemon_name": "pikachu",
                    "evs": {},
                    "ivs": {},
                    "level": 100,
                    "move_name": "Pound",
                },
                "defending": {
                    "pokemon_name": "metapod",
                    "evs": {},
                    "ivs": {},
                    "level": 100,
                },
            },
        )
        assert res.json() == {"min": 14.41, "max": 16.95}
