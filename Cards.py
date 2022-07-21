class Cards:

    @staticmethod
    def grab_deck() -> dict:
        deck = {
            1: [{'N': "soldier"}, {'HP': 2}, {'AP': 1}, {'SP': 1}, {'C': 1}],
            2: [{'N': "monk"}, {'HP': 3}, {'AP': 1}, {'SP': 1}, {'C': 2}],
            3: [{'N': "crab"}, {'HP': 4}, {'AP': 1}, {'SP': 1}, {'C': 3}],
            4: [{'N': "hyena"}, {'HP': 2}, {'AP': 3}, {'SP': 1}, {'C': 3}],
            5: [{'N': "behemoth"}, {'HP': 10}, {'AP': 3}, {'SP': 1}, {'C': 6}],
            6: [{'N': "cyclops"}, {'HP': 6}, {'AP': 4}, {'SP': 1}, {'C': 5}],
            7: [{'N': "dragon"}, {'HP': 10}, {'AP': 10}, {'SP': 1}, {'C': 10}],
            8: [{'N': "reaper"}, {'HP': 2}, {'AP': 10}, {'SP': 1}, {'C': 7}],
            9: [{'N': "bowman"}, {'HP': 1}, {'AP': 2}, {'SP': 1}, {'C': 1}],
            10: [{'N': "prince"}, {'HP': 4}, {'AP': 7}, {'SP': 1}, {'C': 5}]
        }
        return deck

    @staticmethod
    def grab_spells() -> dict:
        spells = {
            1: [{'N': "probation"}, {'E': "target cannot attack for one round"}, {'C': 3}],
            2: [{'N': "tug"}, {'E': "draw an extra 2 cards at the start of next round"}, {'C': 2}],
            3: [{'N': "pulverise"}, {'E': "kill enemy target"}, {'C': 6}],
            4: [{'N': "blind"}, {'E': "enemy target has a 50% chance of attacking one of its own for 2 rounds"}, {'C': 4}],
            5: [{'N': "revive"}, {'E': "resurrect a random card from your graveyard"}, {'C': 5}]
        }
        return spells