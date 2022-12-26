import os
from dataclasses import dataclass

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.query import Query

class DB:
  def __init__(self):
    db = create_engine(DB.db_string())
    self.session = sessionmaker(db)()

  @classmethod
  def db_string(cls):
    USERNAME = os.environ["POSTGRES_USER"]
    PASSWORD = os.environ["POSTGRES_PASSWORD"]
    HOST = os.environ["POSTGRES_HOST"]
    PORT = os.environ["POSTGRES_PORT"]
    DB_NAME = os.environ["POSTGRES_DB"]
    return f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"

@dataclass
class QueryResult:
  result: Query

  # redefine first(), I hate the brackets idk
  @property
  def first(self):
    return self.result.first()

  def first_as_dict(self):
    d = self.first.__dict__
    # remove this key
    d.pop("_sa_instance_state")
    return d
