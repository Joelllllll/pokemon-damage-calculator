from dataclasses import dataclass

from app.db.models.pokemon import PokemonStats
from app.db.models.attack_types import TYPE_MAPPING


@dataclass
class Damage:
  min: int
  max: int

  @classmethod
  def from_damage(cls, damage: int, defending_hp: int):
    # damage can range from 85 - 100 %
    min, max = damage * 0.85, damage
    return cls(round(min / defending_hp * 100.0, 2), round(max / defending_hp * 100.0, 2))

@dataclass
class Battle:
  attacking: PokemonStats
  defending: PokemonStats
  stab: int = 1
  type_advantage = 1

  def __post_init__(self):
    self.check_stab()
    self.type_effectiveness_factor()

  def battle(self):
    # https://bulbapedia.bulbagarden.net/wiki/Damage#Generation_V_onward
    if self.attacking.move.kind == "Physical":
      damage = ( ( self.level_modifier * (self.attacking.attack / self.defending.defense) / 50) + 2 ) * self.type_advantage * self.stab
    if self.attacking.move.kind == "Special":
      damage = ( ( self.level_modifier * (self.attacking.special_attack / self.defending.special_defense) / 50) + 2 ) * self.type_advantage * self.stab

    return Damage.from_damage(damage, self.defending.hp)

  def check_stab(self):
    if self.attacking.move.attack_type in [self.attacking.pokemon.first.type_1, self.attacking.pokemon.first.type_2]:
      self.stab = 1.5

  def type_effectiveness_factor(self):
    move_type = TYPE_MAPPING[self.attacking.move.attack_type]
    # remove Nones
    defending_types = list(filter(None, [self.defending.pokemon.first.type_1, self.defending.pokemon.first.type_2]))

    for def_type in defending_types:
      dt = TYPE_MAPPING[def_type]
      if dt.resists(move_type):
        self.type_advantage *= 0.5
      if dt.weak_to(move_type):
        self.type_advantage *= 2.0

  @property
  def move_attack_type(self):
    return self.attacking.move.attack_type

  @property
  def level_modifier(self):
    return ((2 * self.attacking.level / 5) + 2) * self.attacking.move.power
