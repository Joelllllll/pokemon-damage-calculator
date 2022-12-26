from dataclasses import dataclass, fields
from sqlalchemy import Column, String, Integer, Boolean, func
from sqlalchemy.ext.declarative import declarative_base  

from app.db.db import QueryResult, DB
from app.db.models.moves import Moves

base = declarative_base()

@dataclass
class Pokemon(base):
  __tablename__ = 'pokemon'

  pokemon_number = Column(String)
  pokemon_name = Column(String, primary_key=True)
  type_1 = Column(String)
  type_2 = Column(String)
  total = Column(Integer)
  hp = Column(Integer)
  attack = Column(Integer)
  defense = Column(Integer)
  sp_atk = Column(Integer)
  sp_def = Column(Integer)
  speed = Column(Integer)
  generation = Column(Integer)
  legendary = Column(Boolean)

  @classmethod
  def select_by_name(cls, client, pokemon_name: str):
    return QueryResult(client.query(cls) \
      .where(func.lower(cls.pokemon_name) == func.lower(pokemon_name))
    )

@dataclass
class BaseStats:
  hp: int = 0
  attack: int = 0
  defense: int = 0
  special_attack: int = 0
  special_defense: int = 0
  speed: int = 0

  class StatsValidationError(Exception): pass

  def __post_init__(self):
    self.validate()

  @property
  def max_total_value(self):
    raise NotImplementedError

  @property
  def min_value(self):
    return 0

  @property
  def max_value(self):
    raise NotImplementedError

  def validate(self):
    stat_total = 0
    for field in fields(self):
      val = getattr(self, field.name)
      stat_total += val
      if self.min_value <= val <= self.max_value:
        next
      else:
        raise self.StatsValidationError(f"Value: {val} for field: {field.name} is invalid")
    if stat_total > self.max_total_value:
      raise self.StatsValidationError(f"Stats total {stat_total} is larger than the max allowed total {self.max_total_value}")

@dataclass
class EVs(BaseStats):
# all evs can have values between 0 - 252
# the total must be <= 508

  @property
  def max_total_value(self):
    return 508

  @property
  def max_value(self):
    return 252


@dataclass
class IVs(BaseStats):
  # all ivs can have values between 0 - 31

  @property
  def max_total_value(self):
    return self.max_value * 6

  @property
  def max_value(self):
    return 31


# we also need an object to hold a pokemon post database.
# we need a model that will also include EVs and IVs of a pokemon

@dataclass
class PokemonStats:
  # pokemon field will contain all field from the DB
  # EVs and IVs can change so they are separate
  pokemon_name: str
  evs: EVs
  ivs: IVs
  level: int = 100
  move_name: str = None

  def to_dict(self):
    return {"pokemon": self.pokemon.first_as_dict(),
    "evs": self.evs.__dict__,
    "ivs": self.ivs.__dict__,
    "level": self.level,
    "move_name": self.move_name}

  def __post_init__(self):
    if self.move_name:
      self.move = Moves.select_by_name(DB().session, self.move_name).first
    if self.pokemon_name:
      self.pokemon = Pokemon.select_by_name(DB().session, self.pokemon_name)

  @property
  def hp(self):
    return ((2 * self.pokemon.first.hp + self.ivs.hp + (self.evs.hp / 4)) * self.level / 100) + self.level + 10

  @property
  def attack(self):
    return ( (2 * self.pokemon.first.attack + self.ivs.attack + (self.evs.attack / 4) * self.level / 100) + 5)

  @property
  def defense(self):
    return ( (2 * self.pokemon.first.defense + self.ivs.defense + (self.evs.defense / 4) * self.level / 100) + 5)

  @property
  def special_attack(self):
    return ( (2 * self.pokemon.first.sp_atk + self.ivs.special_attack + (self.evs.special_attack / 4) * self.level / 100) + 5)

  @property
  def special_defense(self):
    return ( (2 * self.pokemon.first.sp_def + self.ivs.special_defense + (self.evs.special_defense / 4) * self.level / 100) + 5)

  @property
  def speed(self):
    return ( (2 * self.pokemon.first.speed + self.ivs.speed + (self.evs.speed / 4) * self.level / 100) + 5)

