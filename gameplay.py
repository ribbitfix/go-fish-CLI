import mastergame
import player

game = mastergame.MasterGame()
game_not_won = True

##def game_over():
##    print game.player_names[game.players[i]] + ", you're out of cards! You won!"
##    game_not_won = False

while game_not_won:
    for i in range(game.number_of_players):
        rank_choice = game.new_turn(game.players[i])
        game.players[i].request_card(game, rank_choice)
        game.players[i].choose_next_move(game)
        if not game.players[i].hand:
            print game.player_names[game.players[i]] + ", you're out of cards! You won!"
            game_not_won = False
            break


##    flag = raw_input("Keep playing? y or n ")
##    if flag == "n":
##        game_not_won = False
