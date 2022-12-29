from __future__ import annotations # allows type hinting in method of enclosing class



class AttackType:
    @classmethod
    def strength(cls):
        "AttackTypes this class hits super effectively"
        raise NotImplementedError

    @classmethod
    def weakness(cls):
        "AttackTypes that hit this class super effectively"
        raise NotImplementedError

    @classmethod
    def resistances(cls):
        "AttackTypes this class takes half damage from"
        raise NotImplementedError

    # only some types have immunities
    @classmethod
    def immune(cls):
        "AttackTypes this class takes no damage from"
        return []

    @classmethod
    def weak_against(cls, attack_type: AttackType) -> bool:
        return attack_type in cls.weakness()

    @classmethod
    def strong_against(cls, attack_type: AttackType) -> bool:
        return attack_type in cls.strength()

    @classmethod
    def immune_to(cls, attack_type: AttackType) -> bool:
        return attack_type in cls.immune()

    @classmethod
    def resists(cls, attack_type: AttackType) -> bool:
        return attack_type in cls.resistances()


class Normal(AttackType):
    @classmethod
    def strength(cls):
        return []

    @classmethod
    def resistances(cls):
        return []

    @classmethod
    def weakness(cls):
        return [Fighting]

    @classmethod
    def immune(cls):
        return [Ghost]


class Fire(AttackType):
    @classmethod
    def strength(cls):
        return [Bug, Grass, Ice, Steel]

    @classmethod
    def resistances(cls):
        return [Fire, Grass, Bug, Ice, Steel, Fairy]

    @classmethod
    def weakness(cls):
        return [Water, Rock, Ground]


class Water(AttackType):
    @classmethod
    def strength(cls):
        return [Fire, Ground, Rock]

    @classmethod
    def resistances(cls):
        return [Fire, Ice, Steel, Water, Grass]

    @classmethod
    def weakness(cls):
        return [Electric, Grass]


class Grass(AttackType):
    @classmethod
    def strength(cls):
        return [Ground, Rock, Water]

    @classmethod
    def resistances(cls):
        return [Grass, Electric, Ground, Water]

    @classmethod
    def weakness(cls):
        return [Fire, Ice, Flying, Bug, Poison]


class Electric(AttackType):
    @classmethod
    def strength(cls):
        return [Flying, Water]

    @classmethod
    def resistances(cls):
        return [Electric, Flying, Steel]

    @classmethod
    def weakness(cls):
        return [Ground]


class Ice(AttackType):
    @classmethod
    def strength(cls):
        return [Dragon, Flying, Grass, Ground]

    @classmethod
    def resistances(cls):
        return [Ice]

    @classmethod
    def weakness(cls):
        return [Fighting, Rock, Fire, Steel]


class Fighting(AttackType):
    @classmethod
    def strength(cls):
        return [Dark, Ice, Normal, Rock, Steel]

    @classmethod
    def resistances(cls):
        return [Dark, Rock, Bug]

    @classmethod
    def weakness(cls):
        return [Fairy, Psychic, Flying]


class Poison(AttackType):
    @classmethod
    def strength(cls):
        return [Fairy, Grass]

    @classmethod
    def resistances(cls):
        return [Fairy, Fighting, Grass, Poison]

    @classmethod
    def weakness(cls):
        return [Ground, Psychic]


class Ground(AttackType):
    @classmethod
    def strength(cls):
        return [Electric, Fire, Poison, Rock, Steel]

    @classmethod
    def resistances(cls):
        return [Poison, Rock]

    @classmethod
    def weakness(cls):
        return [Grass, Water, Ice]

    @classmethod
    def immune(cls):
        return [Electric]


class Flying(AttackType):
    @classmethod
    def strength(cls):
        return [Bug, Fighting, Grass]

    @classmethod
    def resistances(cls):
        return [Bug, Fighting, Grass]

    @classmethod
    def weakness(cls):
        return [Rock, Electric, Ice]

    @classmethod
    def immune(cls):
        return [Ground]


class Psychic(AttackType):
    @classmethod
    def strength(cls):
        return [Fighting, Poison]

    @classmethod
    def resistances(cls):
        return [Psychic, Fighting]

    @classmethod
    def weakness(cls):
        return [Dark, Ghost, Bug]


class Bug(AttackType):
    @classmethod
    def strength(cls):
        return [Grass, Dark, Psychic]

    @classmethod
    def resistances(cls):
        return [Fighting, Grass, Ground]

    @classmethod
    def weakness(cls):
        return [Rock, Fire, Flying]


class Rock(AttackType):
    @classmethod
    def strength(cls):
        return [Bug, Fire, Flying, Ice]

    @classmethod
    def resistances(cls):
        return [Fire, Flying, Normal, Poison]

    @classmethod
    def weakness(cls):
        return [Water, Fighting, Steel, Grass, Ground]


class Ghost(AttackType):
    @classmethod
    def strength(cls):
        return [Ghost, Psychic]

    @classmethod
    def resistances(cls):
        return [Bug, Poison]

    @classmethod
    def weakness(cls):
        return [Ghost, Dark]

    @classmethod
    def immune(cls):
        return [Normal, Fighting]


class Dark(AttackType):
    @classmethod
    def strength(cls):
        return [Ghost, Psychic]

    @classmethod
    def resistances(cls):
        return [Dark, Ghost]

    @classmethod
    def weakness(cls):
        return [Fighting, Fairy, Bug]

    @classmethod
    def immune(cls):
        return [Psychic]


class Dragon(AttackType):
    @classmethod
    def strength(cls):
        return [Dragon]

    @classmethod
    def resistances(cls):
        return [Fire, Water, Grass, Electric]

    @classmethod
    def weakness(cls):
        return [Dragon, Fairy, Ice]


class Steel(AttackType):
    @classmethod
    def strength(cls):
        return [Fairy, Ice, Rock]

    @classmethod
    def resistances(cls):
        return [Bug, Dragon, Flying, Grass, Ice, Psychic, Rock, Steel, Normal]

    @classmethod
    def weakness(cls):
        return [Fire, Ground, Fighting]

    @classmethod
    def immune(cls):
        return [Poison]


class Fairy(AttackType):
    @classmethod
    def strength(cls):
        return [Fighting, Dark, Dragon]

    @classmethod
    def resistances(cls):
        return [Bug, Dark, Fighting]

    @classmethod
    def weakness(cls):
        return [Steel, Poison]

    @classmethod
    def immune(cls):
        return [Dragon]


TYPE_MAPPING = {
    "Normal": Normal,
    "Fire": Fire,
    "Water": Water,
    "Grass": Grass,
    "Electric": Electric,
    "Ice": Ice,
    "Fighting": Fighting,
    "Poison": Poison,
    "Ground": Ground,
    "Flying": Flying,
    "Psychic": Psychic,
    "Bug": Bug,
    "Rock": Rock,
    "Ghost": Ghost,
    "Dark": Dark,
    "Dragon": Dragon,
    "Steel": Steel,
    "Fairy": Fairy,
}
