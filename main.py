from Player import *
import random

USER, BOT = Player("will"), Player()
FIELD_A, FIELD_B = ["none"], ["soldier HP: 2 : AP: 1"]
TURN = 4


def play(count: int = 0, card: bool = True) -> None:

    if card:
        draw(USER)

    USER.add_orb(count)
    USER.grab_hand()

    to_play = input("Pick card to play or pass:\a").casefold()

    if to_play == "pass":
        print(f"card phase passed")
        attack()

    elif USER.check_card(to_play):

        if USER.check_orbs(to_play):
            print(f"{USER.name} played {to_play}!")
            FIELD_A.append(USER.get_card_display(to_play))
            attack()
        else:
            print(f"not enough orbs for {to_play}")
            play(TURN, card=False)
    else:
        print(f"{to_play} does not exist")
        play(TURN, card=False)


def attack() -> None:

    x, y = False, False

    USER.protection(True)
    BOT.protection(True)

    joined = ', '.join(FIELD_A)

    print(f"Available: {joined}")

    to_attack = input("Pick card to attack with or pass:\a").casefold()

    if not FIELD_A:
        USER.protection(False)
    if not FIELD_B:
        BOT.protection(False)

    if to_attack == "pass":
        print(f"turn passed")
        bot_play(TURN)

    elif to_attack in joined:

        print(f"Enemies: {', '.join(FIELD_B)}")

        if (target := input("Pick enemy to attack:\a")) in ', '.join(FIELD_B):
            print(f"{USER.name} attacks with {to_attack}!")
            g, b = USER.offense(to_attack, target)
            if g <= 0:
                print(FIELD_A)
                print(USER.get_card_display(to_attack))
                FIELD_A.pop(FIELD_A.index(USER.get_card_display(to_attack)))
                x = True
            if b <= 0:
                FIELD_B.pop(FIELD_B.index(USER.get_card_display(target)))
                y = True

            tabs = [i for i in joined.split(':') if i.strip().isdigit()]
            USER.mod_deck(to_attack, tabs[0])
            new_j = joined.replace(tabs[0], f" {str(g)} ")

            if not x:
                FIELD_A.pop(FIELD_A.index(USER.get_card_display(to_attack)))

            FIELD_A.append(new_j)

            bot_play(TURN)

        else:
            print("Enemy not available")
            attack()
    else:
        print("Card not available")
        attack()


def bot_play(count: int = 0) -> None:

    draw(BOT)

    global TURN
    TURN += 1

    BOT.add_orb(count)

    for i in BOT.get_hand():
        temp_name = i[0]['N']
        if BOT.check_orbs(temp_name):
            print(f"{BOT.name} played {temp_name}!")
            FIELD_B.append(BOT.get_card_display(temp_name))
            break

    print(f"{BOT.name} finished card phase")

    bot_attack()


def bot_attack() -> None:

    if not FIELD_A:
        pass
    else:

        rand_joined = ''.join(FIELD_B[random.randint(0,len(FIELD_B)-1)])
        rand_attack = rand_joined.split('H')[0].strip()

        print(f"{BOT.name} attacks with {rand_attack}!")

        rand_joint = ''.join(FIELD_A[random.randint(0, len(FIELD_A)-1)])
        rand_target = rand_joint.split('H')[0].strip()

        g, b = BOT.offense(rand_attack, rand_target)

    print(f"{BOT.name} finished attack phase")

    play(TURN)


def draw(n: Player = None, amount: int = 1) -> None:
    print(f"{n.name} is drawing {amount} card")
    n.draw_card(amount)


if __name__ == '__main__':
    FIELD_A.clear()
    play(TURN)
    BOT.add_orb(TURN)
else:
    print("execute from main file")
