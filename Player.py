from Cards import *
from Abilities import *
import random


class Player(Abilities):

    def __init__(self, name: str = "bot"):
        super().__init__()
        self.name: str = name
        self.__health: int = 10
        self.__orbs: int = 0
        self.__deck: list[Card] = Cards.deck()
        self.__spells: list[Spell] = Cards.spells()
        self.__hand: list[Card] = [self.__deck[i + random.randint(0, 6)] for i in range(2)]
        self.__card_data: list[str] = []
        self.__graveyard = [] # TODO: types
        self.__protected: bool = False

        self.__hand.append(self.__spells[random.randint(0, 4)])

    def grab_hand(self) -> int:

        print(f"{self.name}s hand: ")
        print(f"orbs = {self.__orbs}")
        for i in self.__hand:
            print(i.name)
        return 0 # ???

    @property
    def hand(self) -> list[Card]:
        return self.__hand

    def protection(self, shield: bool) -> None:
        self.__protected = shield

    def draw_card(self, amount: int = 0) -> None:
        if random.randint(0,1):
            self.__hand.append(self.__deck[random.randint(0, 9)])
        else:
            self.__hand.append(self.__spells[random.randint(0, 4)])

    def add_data(self, card: str = None) -> None:
        self.__card_data.append(card)

    def rem_data(self, pos: int = None) -> None:
        self.__card_data.pop(pos)

    def check_data(self) -> list:
        return self.__card_data

    def add_orb(self, amount: int = 0) -> int:
        self.__orbs = 0
        self.__orbs += amount
        return self.__orbs

    def rem_orb(self, amount: int = 0) -> int:
        self.__orbs -= amount
        return self.__orbs

    def send_to_graveyard(self, monster: str = None) -> None:
        self.__graveyard.append(monster)

    def check_card(self, tp: str = None) -> int:

        for i in self.__hand:
            if tp == i.name:
                return 1
        return 0

    def check_orbs(self, cd: str = None) -> int:

        temp = self.__deck
        tool = self.__hand
        tes = self.__spells
        for i, v, h in zip(self.__deck, self.__spells, range(len(tool))):
            if i.name == cd:
                if i.c <= self.__orbs:
                    self.rem_orb(i.c)
                    self.add_data(i)
                                            # ! ISSUE HERE with tool.pop([h][0])
                                            # ? I'M NOT ENTIRELY SURE HOW YOUR 
                                            # ? GAME WORKS SO I WILL EXPLAIN IN 
                                            # ? MY PR AND HOPEFULLY YOU CAN FIX 
                                            # ? YOUR ISSUE.
                    tool.pop([h][0]) 
                    return 1

            if v.name == cd:
                if v.c <= self.__orbs:
                    spell = v.name
                    self.rem_orb(v.c)
                    eval(f"self.{spell}(self.name)") # !NONONONONONONONONONONONONO
                    return 1
        return 0

    def mod_deck(self, item: str = None, mod: str = None) -> None:

        for i in self.__deck:
            if i.name == item:
                i.hp = int(mod)

    def get_card_display(self, name: str = None) -> str:

        for i in self.__deck:
            if i.name == name and i.hp:
                return f"{i.name} HP: {i.hp} : AP: {i.ap}"
        return "nil"

    def get_card_details(self, vals: str = None) -> Card:

        for i in self.__deck:
            if vals in i.name:
                return i

    def offense(self, lhs = None, rhs = None) -> tuple[int, int]:

        l_details = self.get_card_details(vals=lhs)
        r_details = self.get_card_details(vals=rhs)

        l_details.hp -= r_details.ap
        r_details.hp -= l_details.ap

        self.evaluate_life(l_details)
        self.evaluate_life(r_details)

        return l_details.hp, r_details.hp

    def evaluate_life(self, details: Card) -> None:
        if details.hp <= 0:
            print(f"{details.name} has been killed!")
            self.send_to_graveyard(details.name)
        else:
            print("%s has %d health remaining!" % (details.name, details.hp))




