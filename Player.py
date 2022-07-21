from Cards import *
from Abilities import *
import random


class Player(Abilities):

    def __init__(self, name: str = "bot"):
        super().__init__()
        self.name = name
        self.__health = 10
        self.__orbs = 0
        self.__deck = Cards.grab_deck()
        self.__spells = Cards.grab_spells()
        self.__hand = [self.__deck[i + random.randint(1,7)] for i in range(2)]
        self.__card_data = []
        self.__graveyard = []
        self.__protected = False

        self.__hand.append(self.__spells[random.randint(1, 5)])

    def grab_hand(self) -> int:

        temp = self.__hand
        print(f"{self.name}s hand: ")
        print(f"orbs = {self.__orbs}")
        for i in range(len(temp)):
            print(f"{temp[i][0]['N']}")
        return 0

    def get_hand(self) -> list:
        return self.__hand

    def protection(self, shield: bool) -> None:
        self.__protected = shield

    def draw_card(self, amount: int = 0) -> None:
        if random.randint(0,1):
            self.__hand.append(self.__deck[random.randint(1, 10)])
        else:
            self.__hand.append(self.__spells[random.randint(1, 5)])

    def add_data(self, card: str = None) -> None:
        self.__card_data.append(card)

    def rem_data(self, pos: int = None) -> None:
        self.__card_data.pop(pos)

    def check_data(self) -> list:
        return self.__card_data

    def add_orb(self, amount: int = 0) -> int:
        self.__orbs += amount
        return self.__orbs

    def rem_orb(self, amount: int = 0) -> int:
        self.__orbs -= amount
        return self.__orbs

    def send_to_graveyard(self, monster: str = None) -> None:
        self.__graveyard.append(monster)

    def check_card(self, tp: str = None) -> int:

        temp = self.__hand
        for i in range(len(temp)):
            if tp in temp[i][0]['N']:
                temp.pop([i][0])
                return 1
        return 0

    def check_orbs(self, cd: str = None) -> int:

        temp = self.__deck
        tes = self.__spells
        for i, v in zip(temp.values(), tes.values()):
            if i[0]['N'] == cd:
                if i[4]['C'] <= self.__orbs:
                    self.rem_orb(i[4]['C'])
                    self.add_data(i)
                    return 1

            if v[0]['N'] == cd:
                if v[2]['C'] <= self.__orbs:
                    spell = v[0]['N']
                    self.rem_orb(v[2]['C'])
                    eval(f"self.{spell}(self.name)")
                    return 1
        return 0

    def mod_deck(self, item: str = None, mod: str = None) -> None:

        temp = self.__deck
        for i in temp.values():
            if i[0]['N'] == item:
                i[1]['HP'] = int(mod)

    def get_card_display(self, name: str = None) -> str:

        temp = self.__deck
        for i in temp.values():
            if i[0]['N'] == name and i[1]['HP']:
                return f"{i[0]['N']} HP: {str(i[1]['HP'])} : AP: {str(i[2]['AP'])}"
        return "nil"

    def get_card_details(self, vals: str = None) -> list:

        for i in self.__deck.values():
            if vals in i[0]['N']:
                return i
        return []

    def offense(self, lhs = None, rhs = None) -> tuple:

        l_details = self.get_card_details(vals=lhs)
        r_details = self.get_card_details(vals=rhs)

        l_details[1]['HP'] -= r_details[2]['AP']
        r_details[1]['HP'] -= l_details[2]['AP']

        if l_details[1]['HP'] <= 0:
            print(f"{l_details[0]['N']} has been killed!")
            self.send_to_graveyard(l_details[0]['N'])
        else:
            print("%s has %d health remaining!" % (l_details[0]['N'], l_details[1]['HP']))

        if r_details[1]['HP'] <= 0:
            print(f"{r_details[0]['N']} has been killed!")
            self.send_to_graveyard(r_details[0]['N'])
        else:
            print("%s has %d health remaining!" % (r_details[0]['N'], r_details[1]['HP']))

        return l_details[1]['HP'], r_details[1]['HP']




