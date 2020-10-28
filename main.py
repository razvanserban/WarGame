from lib.card import Card
from lib.deck import Deck
from lib.player import Player

#DATA SETS
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values =    {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

#GAME SETUP

#define players
player_one = Player('Dodel')
player_two = Player('Costel')

#create and shuffle deck
new_deck = Deck()

for suit in suits:
    for rank in ranks:
        new_deck.set_deck(Card(suit,rank,values[rank]))

new_deck.shuffle_deck()

#split cards to players
for item in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

#GAME PLAY
round_num = 0
game_on = True

while game_on:

    round_num += 1
    print(f'Round {round_num}')

    #check first player cards
    if len(player_one.player_cards) == 0:
        print('Player one out of cards! Player two wins!')
        game_on = False

    #check second player cards
    if len(player_two.player_cards) == 0:
        print('Player two out of cards! Player one wins!')
        game_on = False

    #play new round
    player_one_hand_cards = []
    player_one_hand_cards.append(player_one.remove_one())

    player_two_hand_cards = []
    player_two_hand_cards.append(player_two.remove_one())

    at_war = True

    while at_war:

        if player_one_hand_cards[-1].value > player_two_hand_cards[-1].value:

            player_one.add_cards(player_one_hand_cards)
            player_one.add_cards(player_two_hand_cards)

            at_war = False
        
        elif player_one_hand_cards[-1].value < player_two_hand_cards[-1].value:

            player_two.add_cards(player_one_hand_cards)
            player_two.add_cards(player_two_hand_cards)

            at_war = False

        else:

            print('WAR!')

            #check players have ennough cards to play
            if len(player_one.player_cards) < 5:
                print('Player One unable to play! Player Two wins!')
                game_on = False
                break

            elif len(player_two.player_cards) < 5:
                print('Player Two unable to play! Player One wins!')
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_hand_cards.append(player_one.remove_one())
                    player_two_hand_cards.append(player_two.remove_one())