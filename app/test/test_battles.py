import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from app.db.db import DB
from app.db.models import pokemon, battle


CLIENT = DB().session

class TestBattle:

  def test_move_attack_type(self):
    attacking = pokemon.PokemonStats("Pikachu", pokemon.EVs(), pokemon.IVs(), 100, "Pound")
    defending = pokemon.PokemonStats("Pikachu", pokemon.EVs(), pokemon.IVs(), 100)
    fight = battle.Battle(attacking=attacking, defending=defending)
    assert fight.move_attack_type == "Normal"

  def test_stab_flag(self):
    attacking = pokemon.PokemonStats("Pikachu", pokemon.EVs(), pokemon.IVs(), 100, "Thunder")
    defending = pokemon.PokemonStats("Pikachu", pokemon.EVs(), pokemon.IVs(), 100)
    fight = battle.Battle(attacking=attacking, defending=defending)
    assert fight.stab == 1.5

  def test_type_effectiveness_factor(self):
    attacking = pokemon.PokemonStats("Pikachu", pokemon.EVs(), pokemon.IVs(), 100, "Thunder")
    defending = pokemon.PokemonStats("Pikachu", pokemon.EVs(), pokemon.IVs(), 100)
    fight = battle.Battle(attacking=attacking, defending=defending)
    assert fight.type_advantage == 0.5

  def test_battle(self):
    attacking = pokemon.PokemonStats("Pikachu", pokemon.EVs(), pokemon.IVs(), 100, "Thunder")
    defending = pokemon.PokemonStats("Pikachu", pokemon.EVs(), pokemon.IVs(), 100)
    fight = battle.Battle(attacking=attacking, defending=defending)
    assert fight.battle() == battle.Damage(**{'max': 42.83, 'min': 36.41})

