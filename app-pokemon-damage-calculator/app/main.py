import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from app.db.models.pokemon import EVs, IVs, PokemonStats, StatsPayload, Pokemon
from app.db.models.moves import Moves
from app.db.db import DB
from app.db.models.battle import Battle, PokemonBattlePayload

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
CLIENT = DB()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/pokemon/{pokemon_name}")
def get_pokemon(pokemon_name: str, data: StatsPayload = StatsPayload()) -> dict:
    # EVs and Ivs default to 0 when no supplied
    result = PokemonStats(
        pokemon_name=pokemon_name, evs=EVs(**data.evs), ivs=IVs(**data.ivs)
    )
    return result.to_dict()

@app.get("/pokemon/")
def get_all_pokemon() -> list:
    return Pokemon.all(CLIENT.session)
@app.get("/pokemon-names/")
def get_all_pokemon_names() -> list:
    return Pokemon.all_names(CLIENT.session)

@app.get("/moves/")
def get_all_move_names() -> list:
    return Moves.all_names(CLIENT.session)

@app.post("/battle")
def battle(data: PokemonBattlePayload) -> dict:
    att_pokemon = PokemonStats(
        pokemon_name=data.attacking.pokemon_name,
        evs=EVs(**data.attacking.evs.__dict__),
        ivs=IVs(**data.attacking.ivs.__dict__),
        level=data.attacking.level,
        move_name=data.attacking.move_name,
    )
    def_pokemon = PokemonStats(
        pokemon_name=data.defending.pokemon_name,
        evs=EVs(**data.defending.evs.__dict__),
        ivs=IVs(**data.defending.ivs.__dict__),
        level=data.defending.level,
        move_name=data.defending.move_name,
    )
    fight = Battle(att_pokemon, def_pokemon)
    return fight.battle().__dict__
