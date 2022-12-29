import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from app.db.db import DB
from app.db.models import pokemon

from test.test_main import PIKACHU
from app.db.models.moves import Moves


CLIENT = DB().session


class TestPokemon:
    def test_ev_model(self):
        evs = pokemon.EVs()
        assert evs.__dict__ == {
            "hp": 0,
            "attack": 0,
            "defense": 0,
            "special_attack": 0,
            "special_defense": 0,
            "speed": 0,
        }

    def test_ev_model_error(self):
        with pytest.raises(pokemon.BaseStats.StatsValidationError):
            # max allowed value is 0 - 252
            pokemon.EVs(hp=1000)

    def test_iv_model(self):
        ivs = pokemon.IVs()
        assert ivs.__dict__ == {
            "hp": 0,
            "attack": 0,
            "defense": 0,
            "special_attack": 0,
            "special_defense": 0,
            "speed": 0,
        }

    def test_iv_model_error(self):
        with pytest.raises(pokemon.BaseStats.StatsValidationError):
            # max allowed value is 0 - 31
            pokemon.IVs(hp=40)


PIKACHU = {
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
}


class TestPokemonStats:
    def test_init(self):
        result = pokemon.PokemonStats(
            "pikachu", pokemon.EVs(), pokemon.IVs(), 100, "Pound"
        )
        assert result.pokemon.first == pokemon.Pokemon(**PIKACHU)
        assert result.evs == pokemon.EVs()
        assert result.ivs == pokemon.IVs()
        # check move lookup was done correctly
        assert result.move == Moves.select_by_name(CLIENT, "Pound").first

    def test_hp_stat(self):
        result = pokemon.PokemonStats(
            "Pikachu", pokemon.EVs(hp=200), pokemon.IVs(hp=31), 100, "Pound"
        )
        assert result.hp == 261

    def test_attack_stat(self):
        result = pokemon.PokemonStats(
            "Pikachu", pokemon.EVs(attack=200), pokemon.IVs(attack=31), 100, "Pound"
        )
        assert result.attack == 196

    def test_defense_stat(self):
        result = pokemon.PokemonStats(
            "Pikachu", pokemon.EVs(defense=200), pokemon.IVs(defense=31), 100, "Pound"
        )
        assert result.defense == 166

    def test_special_attack_stat(self):
        result = pokemon.PokemonStats(
            "Pikachu",
            pokemon.EVs(special_attack=200),
            pokemon.IVs(special_attack=31),
            100,
            "Pound",
        )
        assert result.special_attack == 186

    def test_special_defense_stat(self):
        result = pokemon.PokemonStats(
            "Pikachu",
            pokemon.EVs(special_defense=200),
            pokemon.IVs(special_defense=31),
            100,
            "Pound",
        )
        assert result.special_defense == 186

    def test_speed_stat(self):
        result = pokemon.PokemonStats(
            "Pikachu", pokemon.EVs(speed=200), pokemon.IVs(speed=31), 100, "Pound"
        )
        assert result.speed == 266

    def test_max_ev_values(self):
        # max value for Evs are  252
        evs = pokemon.EVs(hp=100, attack=252)
        assert evs.__dict__ == {
            "attack": 252,
            "defense": 0,
            "hp": 100,
            "special_attack": 0,
            "special_defense": 0,
            "speed": 0,
        }

    def test_max_ev_values_error(self):
        with pytest.raises(pokemon.BaseStats.StatsValidationError):
            pokemon.EVs(hp=100, attack=253)

    def test_max_iv_values(self):
        # max value for Ivs are  21
        ivs = pokemon.IVs(hp=31, attack=31)
        assert ivs.__dict__ == {
            "attack": 31,
            "defense": 0,
            "hp": 31,
            "special_attack": 0,
            "special_defense": 0,
            "speed": 0,
        }

    def test_max_iv_values_error(self):
        with pytest.raises(pokemon.BaseStats.StatsValidationError):
            pokemon.IVs(hp=32, attack=21)
