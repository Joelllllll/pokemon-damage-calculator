import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from app.db.models.attack_types import *


class TestAttackTypes:
  def test_resistances(self):
    assert Water.resists(Fire)
    assert Fire.resists(Bug)
    assert Ice.resists(Ice)
    assert Dragon.resists(Grass)
    assert Fire.resists(Fairy)
    assert Steel.resists(Psychic)
    assert not Normal.resists(Fighting)

  def test_weakness(self):
    assert Water.weak_to(Grass)
    assert Fire.weak_to(Ground)
    assert Electric.weak_to(Ground)
    assert Ice.weak_to(Steel)
    assert Dragon.weak_to(Dragon)
    assert Ghost.weak_to(Dark)
    assert Dark.weak_to(Bug)
    assert not Normal.weak_to(Dark)

  def test_strengths(self):
    assert Fire.strong_against(Grass)
    assert Grass.strong_against(Water)
    assert Electric.strong_against(Flying)
    assert Psychic.strong_against(Fighting)
    assert Fighting.strong_against(Dark)
    assert Fairy.strong_against(Dragon)
    assert Steel.strong_against(Fairy)
    assert not Ground.strong_against(Grass)

  def test_immunity(self):
    assert Ghost.immune_to(Normal)
    assert Normal.immune_to(Ghost)
    assert Steel.immune_to(Poison)
    assert Flying.immune_to(Ground)
    assert Ground.immune_to(Electric)
    assert Fairy.immune_to(Dragon)
    assert not Ghost.immune_to(Dark)
