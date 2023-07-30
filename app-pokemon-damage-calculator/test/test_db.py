import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from app.db.models.moves import Moves
from app.db.models.pokemon import Pokemon
from app.db.db import DB


CLIENT = DB()

PIKACHU = {
    "pokemon_number": 25,
    "type_1": "Electric",
    "total": 320,
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


class TestDB:
    def test_select_by_name_move(self):
        move = Moves.select_by_name(CLIENT.session, "Pound")
        assert move.result.count() == 1
        move = move.first
        assert move.move_name == "Pound"
        assert move.effect == "Deals damage with no additional effect."
        assert move.attack_type == "Normal"
        assert move.kind == "Physical"
        assert move.power == 40
        assert move.accuracy == "100%"
        assert move.pp == 35

    def test_select_by_name_pokemon(self):
        pokemon = Pokemon.select_by_name(CLIENT.session, "Pikachu")
        assert pokemon.result.count() == 1
        pokemon = pokemon.first
        assert pokemon.pokemon_name == "Pikachu"
        assert pokemon.type_1 == "Electric"
        assert pokemon.type_2 == None
        assert pokemon.total == 320
        assert pokemon.hp == 35
        assert pokemon.attack == 55
        assert pokemon.defense == 40
        assert pokemon.sp_atk == 50
        assert pokemon.sp_def == 50
        assert pokemon.speed == 90
        assert pokemon.generation == 1
        assert pokemon.legendary == False

    def test_first_as_dict_pokemon(self):
        pokemon = Pokemon.select_by_name(CLIENT.session, "Pikachu")
        pokemon_dict = pokemon.first_as_dict()
        assert pokemon_dict == PIKACHU
