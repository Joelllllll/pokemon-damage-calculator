from __future__ import annotations

from dataclasses import dataclass

from app.db.models.pokemon import PokemonStats
from app.db.models.attack_types import TYPE_MAPPING

from fastapi import HTTPException


@dataclass
class Damage:
    min: int
    max: int

    @classmethod
    def from_damage(cls, damage: int, defending_hp: int) -> Damage:
        # damage can range from 85 - 100 %
        min, max = damage * 0.85, damage
        return cls(
            round(min / defending_hp * 100.0, 2), round(max / defending_hp * 100.0, 2)
        )


@dataclass
class Battle:
    attacking: PokemonStats
    defending: PokemonStats
    stab: int = 1
    type_advantage = 1

    PHYSCIAL_ATTACK = "Physical"
    SPECIAL_ATTACK = "Special"

    def __post_init__(self):
        self.validate()
        self.check_stab()
        self.type_effectiveness_factor()

    def validate(self):
        "Validate the move name and pokemon name"
        if not self.attacking.move_name:
            raise HTTPException(status_code=400, detail=f"Move not found: '{self.attacking.move.name}'")
        if not self.attacking.pokemon_name:
            raise HTTPException(status_code=400, detail=f"Pokemon not found: '{self.attacking.pokemon.name}'")

    # Damage formulas used were copied from here, idk how the pokemon devs came up with it
    # https://bulbapedia.bulbagarden.net/wiki/Damage#Generation_V_onward
    def battle(self) -> Damage:
        "Uses the formulas from the above URL to calc min/max damage"
        if self.attacking.move.kind == self.PHYSCIAL_ATTACK:
            damage = (
                (
                    (
                        self.level_modifier
                        * (self.attacking.attack / self.defending.defense)
                        / 50
                    )
                    + 2
                )
                * self.type_advantage
                * self.stab
            )
        if self.attacking.move.kind == self.SPECIAL_ATTACK:
            damage = (
                (
                    (
                        self.level_modifier
                        * (
                            self.attacking.special_attack
                            / self.defending.special_defense
                        )
                        / 50
                    )
                    + 2
                )
                * self.type_advantage
                * self.stab
            )

        return Damage.from_damage(damage, self.defending.hp)

    def check_stab(self) -> float:
        "If the movoes attack type matches any of the pokemons types it gets a 1.5 times multiplier"
        if self.attacking.move.attack_type in [
            self.attacking.pokemon.first.type_1,
            self.attacking.pokemon.first.type_2,
        ]:
            self.stab = 1.5

    def type_effectiveness_factor(self) -> float:
        "Compares the attacking move to the denending types for a damage multiplier, can range from 1/4 -> 4"
        move_type = TYPE_MAPPING[self.attacking.move.attack_type]
        # not all pokemon have 2 types, remove None from list
        defending_types = list(
            filter(
                None,
                [
                    self.defending.pokemon.first.type_1,
                    self.defending.pokemon.first.type_2,
                ],
            )
        )

        for def_type in defending_types:
            dt = TYPE_MAPPING[def_type]
            if dt.resists(move_type):
                self.type_advantage *= 0.5
            if dt.weak_against(move_type):
                self.type_advantage *= 2.0
            if dt.immune_to(move_type):
                self.type_advantage *= 0.0

    @property
    def move_attack_type(self) -> str:
        return self.attacking.move.attack_type

    @property
    def level_modifier(self) -> float:
        return ((2 * self.attacking.level / 5) + 2) * self.attacking.move.power
