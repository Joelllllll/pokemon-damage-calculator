import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from app.db.models.attack_types import *


class TestAttackTypes:
    def test_resistances_2(self):
        # ChatGPT generated all type interactions seen in this file, it has probably missed some
        type_resistances = [
            (Fire, Bug), (Fire, Steel), (Fire, Fairy),
            (Water, Fire), (Water, Water), (Water, Ice), (Water, Steel),
            (Electric, Electric), (Electric, Flying), (Electric, Steel),
            (Grass, Water), (Grass, Electric), (Grass, Grass), (Grass, Ground),
            (Ice, Ice),
            (Fighting, Bug), (Fighting, Rock), (Fighting, Dark),
            (Poison, Grass), (Poison, Fairy), (Poison, Poison),
            (Ground, Poison), (Ground, Rock),
            (Flying, Grass), (Flying, Fighting), (Flying, Bug),
            (Psychic, Fighting), (Psychic, Psychic),
            (Bug, Grass), (Bug, Fighting), (Bug, Ground),
            (Rock, Normal), (Rock, Fire), (Rock, Poison), (Rock, Flying),
            (Ghost, Poison), (Ghost, Bug),
            (Dragon, Electric), (Dragon, Water), (Dragon, Grass), (Dragon, Fire),
            (Dark, Ghost), (Dark, Dark),
            (Steel, Normal), (Steel, Grass), (Steel, Ice), (Steel, Flying),
            (Steel, Psychic), (Steel, Bug), (Steel, Dragon), (Steel, Steel), (Steel, Fairy),
            (Fairy, Fighting), (Fairy, Bug), (Fairy, Dark)
        ]
        for type1, type2 in type_resistances:
            assert type1.resists(type2)


    def test_weakness_2(self):
        weaknesses = [
            (Water, Grass), (Water, Electric),
            (Fire, Water), (Fire, Rock), (Fire, Ground),
            (Grass, Bug), (Grass, Fire), (Grass, Ice),
            (Electric, Ground),
            (Ice, Fighting), (Ice, Fire), (Ice, Rock), (Ice, Steel),
            (Fighting, Flying), (Fighting, Psychic), (Fighting, Fairy),
            (Poison, Ground), (Poison, Psychic),
            (Ground, Water), (Ground, Ice),
            (Flying, Electric), (Flying, Ice), (Flying, Rock),
            (Psychic, Bug), (Psychic, Ghost), (Psychic, Dark),
            (Bug, Fire), (Bug, Flying), (Bug, Rock),
            (Rock, Water), (Rock, Grass), (Rock, Fighting),
            (Ghost, Ghost), (Ghost, Dark),
            (Dragon, Ice), (Dragon, Fairy), (Dragon, Dragon),
            (Dark, Fighting), (Dark, Bug),
            (Steel, Fighting), (Steel, Ground), (Steel, Fire),
            (Fairy, Poison), (Fairy, Steel),
        ]

        for type1, type2 in weaknesses:
            assert type1.weak_against(type2)

    def test_immunities(self):
        immunities = [
            (Ghost, Normal),
            (Normal, Ghost),
            (Steel, Poison),
            (Flying, Ground),
            (Ground, Electric),
            (Normal, Ghost),
            (Dark, Psychic),
            (Fairy, Dragon),
        ]

        for type1, type2 in immunities:
            assert type1.immune_to(type2)
