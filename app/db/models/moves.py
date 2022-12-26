from dataclasses import dataclass

from sqlalchemy import Column, String, Integer, func
from sqlalchemy.ext.declarative import declarative_base  

from app.db.db import QueryResult

base = declarative_base()


# class for moves table in postgres database
@dataclass
class Moves(base):
  __tablename__ = 'pokemon_moves'

  move_number = Column(String, primary_key=True)
  move_name = Column(String)
  effect = Column(String)
  attack_type = Column(String)
  kind = Column(String)
  power = Column(Integer)
  accuracy = Column(String)
  pp = Column(Integer)

  @classmethod
  def select_by_name(cls, client, move_name: str):
    return QueryResult(client.query(cls) \
      .where(func.lower(cls.move_name) == func.lower(move_name))
    )

