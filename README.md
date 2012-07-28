Go Fish CLI
===========
This was the final assignment for an intro to programming class taught by Jeff Schwaber in the spring of 2011. There's a *lot* of room for improvement here, but it was a good learning exercise.

Below are the notes I kept while working on the project. They weren't intended for an audience beyond myself, so they might be a little cryptic, but hopefully they'll give you a sense of my thought process. (This was before I started using git, when my version control system was to save a new copy of the files at key points in the process, so the headings - "cardGame1", "cardGame2" and so on - refer to the directory I was working in at the time.)

PROCESS NOTES:
--------------
cardGame1 (starting over on the Mac after the Dell died)
---------
### Sun 5/22
* Created CardDeck and Player classes with one method each (prepare_deck and pick_a_card)
* Created game01 to get them talking to each other. No dice.

### Mon 5/23
* The problem yesterday: I forgot about specifying the module name when referring to its methods (eg. turtle.forward() )
* Problem: "deck" is an object, not a list, so it doesn't have a pop method. Tried moving "deck=[ ]" outside of the prepare_deck function, so I would have access to it, but then the function didn't recognize it: 
    deck.append((i, j))
    NameError: global name 'deck' is not defined
* Solution: make deck = prepare_deck() instead of CardDeck object.
* Problem: trying to call the pick_a_card function from within the draw_a_hand function, but the deck isn't getting passed to pick_a_card so it's popping from an empty list.

cardGame2 (starting over after Jeff's lecture on objects)
---------
### Mon 5/23 cont'd
- Created MasterGame class with attributes: deck, number_of_players. Migrated prepare_deck method to this class.
- Updated Player class:
    - Created init method with attributes: hand, number_of_cards
    - Fixed draw_a_hand method
        - Changed the while loop to a for loop
        - Got internal method call working, but I'm not sure how.
- Renamed modules according to naming conventions (all lowercase rather than camelCase)
- Reviewed old code written in Windows
    - Added add_card_to_hand method to Player class; revised draw_a_hand method to call it.
    - Simplified method names: draw_card, draw_hand
- NEXT TASK: elaborate on MasterGame constructor

### Sun 5/29
- Made additions to MasterGame constructor:
    - self.prepare_deck()
    - a for loop to create player objects
- couldn't figure out how to access the objects after creating them; thought maybe the game constructor wasn't the place to create player objects after all and tried to make it happen in the gameplay file instead; had the same problem
    - consulted internet: http://stackoverflow.com/questions/4010840/generating-variable-names-on-fly-in-python and ...1060090/changing-variable-names-with-python-for-loops
    - created players list to contain player objects so they can be accessed by index number
- NEXT TASK: figure out what to do with the players now that i've got them.
- added to game constructor: a for loop to deal a hand to each player
- added discard_pile attribute to game constructor and and discard method to Player class
- added view_hand method to Player class
- Discovered that the 2nd player is dealt the 1st player's hand plus 7 more cards.
    - Thought the loop might be the problem; called draw_hand for each player separately in the gameplay file - got the same result.
- NEXT TASK: WTF, draw_hand method?

### Thurs 6/2
- I thought maybe the MasterGame constructor loop to create player objects was the problem; commented it out and created the players in gameplay instead. Didn't help.
- Removed "hand = [ ]" from the Player constructor arguments; this fixed the problem! Not sure why.

cardGame3
---------
Realized there was no way to change the number of cards in a hand in the MasterGame constructor. Decided to remedy this by:
- Adding a "size_of_hand" argument to the MasterGame constructor.
- Creating a "deal_hand" method in MasterGame, to replace the current "draw_hand" method in Player. (NEXT TASK.)

### Fri 6/3
- renamed "size_of_hand" to "cards_per_hand"
- GENERAL QUESTION: When to use "return" at the end of a function?
- Created deal_hand method; added it to the "create player objects" loop.
- Got rid of "deal a hand to each player" loop and Player draw_hand method.
- revised view_hand method so it lists each card on a separate line.
- created search_hand method
- revised Player constructor:
    - removed number_of_cards argument/attribute
	- added played_cards list
- created play_pair method

### Sat 6/4
figured out how to use input function to provide argument for search_hand method

cardGame4
---------
Current search_hand method felt like a dead-end: couldn't figure out how to make it interact with both the active player and opponent player objects. So, some reorganizing:
- created select_card_from_hand method
- created request_card function which calls select_card on another player object
    - tried using "rank=input("What rank do you want? ") as a parameter, but it fucks everything up. WHY DOESN'T THIS WORK?
NEXT TASK: expand request_card method to include next actions.
- Expanded request_card method to add card to player's hand and show it to them.
- Created choose_next_move method to keep the request_card method from sprawling. 
- Input that's not in the form of a datatype or a recognized name causes an error. I guess I need to CREATE AN EXCEPTION here? (6/6: changed from input() to raw_input(); made 1 and 2 into strings.)
NEXT TASKS:
- start_turn method in MasterGame
- complete choose_next_move method in Player

### Sun 6/5
- To create a way for the game to address each player:
	- changed self.players from a list to a dictionary in MasterGame constructor
	- changed "create player objects" loop to add players to the dictionary
- NEXT TASK: learn about dictionaries. Should the player object be the key or the value? (Right now it's the key.)
	- It also works as the value.
- Maybe I need a player list too, though, since dictionaries are unordered?

### Mon 6/6
- Added players list back; renamed dictionary player_names, made player objects the keys and player names the values.
- Wrote start_turn method
- PROBLEM: "other_player = self.players.index(player) + 1" is only going to work for players[0], duh. So how do I make it cycle back around to the beginning of the list?
	- Fixed this with an if-else statement. Jeff sez I could also use a LINKED LIST.
- Revised select_card_from_hand per Jeff's suggestion: changed "if rank in card" to "if rank == card[0]" because it's more precise and therefore less likely to cause problems.
- NEXT TASK: reorganize code per Jeff's suggestion: have an "above function" to contain the simpler functions instead of having one function lead into the next.

cardGame5 (reorganizing code per Jeff's suggestion, above)
---------
### Thurs 6/9
- removed show_hand from request_card (not necessary - hand is still visible.)
- tested start_turn method; changed name to new_turn
- NEXT TASK: maybe try making other_player and rank return values that can be passed to request_card method???

### Sat 6/11
- cleaned up new_turn method:
	- made other_player and rank into return values
		- it worked, but returned them as a single value (a tuple?), so they couldn't be passed as arguments to the request card method. So:
		- moved "other_player" business to request_card method and made some changes to make it work, e.g. added "game" as a parameter so the method would have access to the player list and deck (regarding the deck: WHY WASN'T THIS AN ISSUE BEFORE?)
	- eliminated a couple lines of code by getting rid of unnecessary variables (player_name, rank)
- wrote choose_next_move method
- QUESTION: how to get rid of redundancy in choose_next_move method?
	- (Partial?) answer: move redundant code into a separate method: wrote remove_card_from_hand
- Added remove_card_from_(other player's)_hand to request_card method
- Got rid of play_pair method
NEXT TASKS:
	- maybe get rid of one-line methods, add_card_to_hand and discard?
	- maybe rename select_card_from_hand so it's not so close to remove_card_from_hand? (Or combine the two? Probably not...)
	- create gameplay loop for continuous play...
- Got rid of draw_card, add_card_to_hand, and discard methods.
- Added "Your played cards are..." to choose_next_move method
- Renamed select_card_from_hand as search_hand
- Created game loop. Inside "while game_not_won" loop, the "for player in game.players" loop is intended to cycle through the player list. However:
	- PROBLEM: AttributeError: MasterGame instance has no attribute 'player'

### Sun 6/12
- Consulted http://docs.python.org/tutorial/controlflow.html#for-statements
- Changed "for player in game.players" to "for i in range(game.number_of_players)" and "game.player" statements to "game.players[i]"
- IT WORKS! NEXT TASK: add code to "flag" block to determine if the game has been won.

cardGame6 (made it work; will now attempt to make it good)
---------
- Consulted internet and learned that an empty list is falsy in Python.
- added "if not game.players[i].hand" section to end of for loop.
- discovered use case where one player gives away last card on other player's turn
	- added conditional to beginning of for loop to handle this case
	- PROBLEM: this solution doesn't work for more than 2 players
- created game_over function to contain otherwise redundant code; didn't work. NOT SURE WHY.
- NEXT TASK: solve above problem.

cardGame7
---------
### Mon 6/13
- To solve the above problem, I need to reuse the "identify other player" code from the request_card method. So maybe move it into a separate MasterGame method?
- Wrote identify_other_player function. NEXT TASK: implement and test.

TODO:
-----
* deal with exceptions
* use sort method to organize each player's hand?
* find a way to prevent players from seeing each other's hands
* show top card in discard pile so players can select it?
* Fix "Your played cards are..." so it only displays the most recently played pair

