class Player:
    def __init__(self):
        self.hand = []
        self.played_cards = []
        
    def view_hand(self):
        for card in self.hand:
            print card
            
    def request_card(self, game, rank):
        #identify other player
        if game.players.index(self) < game.number_of_players - 1:
            other_player = game.players[game.players.index(self) + 1]
        else:
            other_player = game.players[0]
        #check other player's hand; receive card or draw from deck
        if other_player.search_hand(rank):
            print "Success!"
            card = other_player.remove_card_from_hand(rank)
        else:
            print "Go fish!"
            card = game.deck.pop()
        self.hand.append(card)
        print "Your new card is " + str(card)
            
    def search_hand(self, rank):
        for card in self.hand:
            if rank == card[0]:              
                return card

    def remove_card_from_hand(self, rank):
        card = self.search_hand(int(rank))
        self.hand.remove(card)
        return card

    def choose_next_move(self, game):
        choice = raw_input("Would you like to play a pair (1) or discard (2)? ")
        if choice == "1":
            rank = raw_input("What rank would you like to play? ")
            for i in range(2):
                card = self.remove_card_from_hand(rank)
                self.played_cards.append(card)
            print "Your played cards are:", self.played_cards
        elif choice == "2":
            rank = raw_input("What rank would you like to discard? ")
            card = self.remove_card_from_hand(rank)
            game.discard_pile.append(card)
        else:
            print "Please type either 1 or 2."
            self.choose_next_move(game)

