'''
Deck Class
'''

from random import shuffle

class Deck:

    def __init__ (self):
        self.all_cards = []

    def set_deck(self, card):
        self.all_cards.append(card)

    def get_deck(self):
        return self.all_cards

    def shuffle_deck(self):
        shuffle(self.all_cards)
        return self.all_cards
    
    def deal_one(self):
        return self.all_cards.pop()