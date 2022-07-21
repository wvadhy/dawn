class Abilities:

    def __init__(self):
        self._probed = False
        self._extra_cards = False
        self.blinded = False

    def probation(self, target: str = None) -> None:
        print(f"{target} is unable attack for 1 round")
        self._probed = True

    def tug(self, person: str = None) -> None:
        print(f"{person} will draw two extra cards at the start of next round")
        self._extra_cards = True

    def blind(self, target: str = None) -> None:
        print(f"{target} has a 50% chance of attacking an ally for 2 rounds")
        self.blinded = True

