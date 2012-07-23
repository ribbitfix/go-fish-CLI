import random
import player

class MasterGame:
    def __init__(self, number_of_players=2, cards_per_hand=7):
        self.number_of_players = number_of_players
        self.cards_per_hand = cards_per_hand
        self.deck = []
        self.discard_pile = []
        self.players = []
        self.player_names = {}

        self.prepare_deck()

        #create player object, add to list, assign name and deal hand
        for i in range(number_of_players):
            p = player.Player()
            self.players.append(p)
            self.player_names[p] = "Player " + str(i+1)
            self.deal_hand(p)

    def prepare_deck(self):
        for i in range(2, 15):
            for j in ['Hearts', 'Spades', 'Diamonds', 'Clubs']:
                self.deck.append((i, j))
        random.shuffle(self.deck)
        return self.deck

    def deal_hand(self, player):
        for i in range(self.cards_per_hand):
            card = self.deck.pop()
            player.hand.append(card)

    def new_turn(self, player):
        print "-"*35
        raw_input(self.player_names[player] + ", press return to continue.")
        print "Your hand is:"
        player.view_hand()
        return input("What rank do you want to ask for? ")

    def identify_other_player(self, player):
        if self.players.index(player) < self.number_of_players - 1:
            other_player = self.players[self.players.index(player) + 1]
        else:
            other_player = self.players[0]
        return other_player
    
        
