import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
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
        assert Water.weak_against(Grass)
        assert Fire.weak_against(Ground)
        assert Electric.weak_against(Ground)
        assert Ice.weak_against(Steel)
        assert Dragon.weak_against(Dragon)
        assert Ghost.weak_against(Dark)
        assert Dark.weak_against(Bug)
        assert not Normal.weak_against(Dark)

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
