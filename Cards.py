class Card:
    
    def __init__(self, name, hp, ap, sp, c):
        self.name = name
        self.hp = hp
        self.ap = ap
        self.sp = sp
        self.c = c

class Spell:

    def __init__(self, name, desc, c):
        self.name = name
        self.desc = desc
        self.c = c

class Cards:

    _deck = [
        Card("monk", 3, 1, 1, 2),
        Card("soldier", 2, 1, 1, 1),
        Card("crab", 4, 1, 1, 3),
        Card("hyena", 2, 3, 1, 3),
        Card("behemoth", 10, 3, 1, 6),
        Card("cyclops", 6, 4, 1, 5),
        Card("dragon", 10, 10, 1, 10),
        Card("reaper", 2, 10, 1, 7),
        Card("bowman", 1, 2, 1, 1),
        Card("prince", 4, 7, 1, 5)
    ]

    @staticmethod
    def deck() -> dict: 
        return Cards._deck.copy()

    _spells = [
        Spell("probation", "target cannot attack for one round", 3),
        Spell("tug", "draw an extra 2 cards at the start of next round", 2),
        Spell("pulverise", "kill enemy target", 6),
        Spell("blind", "enemy target has a 50% chance of attacking one of its own for 2 rounds", 4),
        Spell("revive", "resurrect a random card from your graveyard", 5)
    ]

    @staticmethod
    def spells() -> dict:
        return Cards._spells.copy()

