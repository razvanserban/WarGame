'''
Class Player
'''

class Player:

    def __init__(self, name):
        self.name = name
        self.player_cards = []

    def remove_one(self):
        return self.player_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # add multiple cards
            self.player_cards.extend(new_cards)
        else:
            #add single card
            self.player_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.player_cards)} cards'