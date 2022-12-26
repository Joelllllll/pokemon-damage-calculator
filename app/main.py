from dataclasses import dataclass
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from app.db.models.pokemon import Pokemon, EVs, IVs, PokemonStats
from app.db.db import DB
from app.db.models.battle import Battle

from fastapi import FastAPI

app = FastAPI()
CLIENT = DB()


## Probably move these dataclasses to a battle.py model?
@dataclass
class Stats:
    evs: dict
    ivs: dict

@dataclass
class PokemonBattle:
    attacking: PokemonStats
    defending: PokemonStats


@app.get("/pokemon/{pokemon_name}")
def get_pokemon(pokemon_name: str, data: Stats = None):
    # EVs and Ivs default to 0 when no supplied
    result = PokemonStats(pokemon_name=pokemon_name, evs=EVs(**data.evs), ivs=IVs(**data.ivs))
    return result.to_dict()

@app.post("/battle")
def battle(data: PokemonBattle):
    # build up the att and def pokemon objects
    att_pokemon = PokemonStats(pokemon_name=data.attacking.pokemon_name, evs=EVs(**data.attacking.evs.__dict__), ivs=IVs(**data.attacking.ivs.__dict__), level=data.attacking.level, move_name=data.attacking.move_name)
    def_pokemon = PokemonStats(pokemon_name=data.defending.pokemon_name, evs=EVs(**data.defending.evs.__dict__), ivs=IVs(**data.defending.ivs.__dict__), level=data.defending.level, move_name=data.defending.move_name)
    fight = Battle(att_pokemon, def_pokemon)
    return fight.battle().__dict__