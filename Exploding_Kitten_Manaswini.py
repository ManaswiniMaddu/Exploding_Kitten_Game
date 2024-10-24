 # Manaswini Maddu - CS 524
# Exploiding Kittens Game
# This game can only be played by 2 to 5 players
# Language used: Python 3
# Name of the file: Exploding_kitten_Manaswini.py
""" 
Description or Rules of the Game:
SETUP: 
      Initially the deck consists of 4 ATTACK cards, 4 SHUFFLE cards, 4 SKIP cards, 5 SEE THE FUTURE cards.
      The DEFUSE cards and EXPLOIDING KITTEN cards are separated from the deck.
      Consider only 2 DEFUSE cards if players are 2 or 3 else consider 6 DEFUSE cards.
      Consider EXPLOIDING KITTEN cards of (players-1).
      Each player is given randomly the 7 cards from the intial deck and 1 DEFUSE card.
      Then the remmaining DEFUSE cards and EXPLOIDING KITTENS cards are inserted back to deck and shuffled.
TURN RULES:
      Start the game with a player.
      This player can/cannot play any number of action cards that he/she wishes to.
      The player turn ends by drawing a card from the deck 
      The player game ends when the card drawn is EXPLOIDING KITTENS and that particular player doesn't have DEFUSE card with them.
      The game continues until a single player is left in the game. And the last standing player wins the GAME!

ACTION CARD RULES: If the card played is of particular name, it will perform those actions as below.
SHUFFLE:           Randomly shuffles the deck.
SEE THE FUTURE:    The current player can secretly see the top the 3 cards of the deck and put them back.
CAT CARDS:         If pair of two same type of cat cards are dropped, you can choose one random card from any one player that you wish to take.
                  Here the type of cat cards used are: TacoCat, Beard Cat, Rainbow-Ralphing Cat, Cattermelon, Hairy Potato Cat.
FAVOR:             You can select a player to take a card from his hand. The other player decides which card to give.
ATTACK:           No need to draw any card from the deck. Next player should take 2 turns in a row.
SKIP:             End your turn without drawing card from deck.
ATTACK + SKIP:    If SKIP is played as a defense to an ATTACK card from previous player, it ends only 1 of the 2 turns. 2 skip cards can end both turns.
EXPLOIDNG KITTEN: You have to show immediately if you receive this card.
                  You will lose the game if you don't have DEFUSE card in your hand.
DEFUSE:           Take the EXPLOIDNG KITTEN card you drew and insert at any position in the deck that you wish to. You can continue to play the game. 
Social handling: 
1. If a player draws an exploding kitten, they are forced use a defuse card if they have one. 
2. When a player is attacked, instead of implemented “play(n times), draw_one_card, play(n times), draw_one_card” as two Tuens, 
the current implementation is “play(n times), draw_one_card, draw_one_card

NOTE: Originally, this game also gas a NOPE card, and additionl features of “special combos” which are not implemented as part of this game.
"""
# Importing random library to shuffle elements randomly
import random

# Initialization with player names 
class Card:
  def __init__(self, name):
    self.name = name

# Preparing Deck
# Initialization of deck by taking number of players and type of cards
class Deck:
  def __init__(self, num_players):
    self.cards = []
    self.num_players = num_players
    self.cat_cards = ['Taco Cat', 'Beard Cat', 'Rainbow-Ralphing Cat', 'Cattermelon', 'Hairy Potato Cat']

  # Intial deck creation
  # Initial deck does not contain exploding kittens and defuse cards.
  # We will add them later after distributing the following cards.
  def create_initial_deck(self):
    for i in range(4):
      self.cards.append(Card('Attack'))
      self.cards.append(Card('Skip'))
      self.cards.append(Card('Favor'))
      self.cards.append(Card('Shuffle'))
      self.cards.append(Card('See The Future'))
      for name in self.cat_cards:
        self.cards.append(Card(name))

  # Adds the defuse cards and exploding kittens back to the deck
  # after distributing the initial cards to players.
  def add_remaining_cards(self):
    num_defuse = 0
    # Calculate the number of defuse cards to be inlcuded in the
    # game depending on the number of players.
    if self.num_players == 2 or self.num_players == 3:
      num_defuse = 2
    else:
      num_defuse = 6 - self.num_players

    for i in range(self.num_players -1):
      self.cards.append(Card('Exploding Kitten'))

    for i in range(num_defuse):
      self.cards.append(Card('Defuse'))

  # To shuffle randomly the deck
  def shuffle_deck(self):
    random.shuffle(self.cards)

  # To draw card from deck
  def draw_card(self):
    return self.cards.pop(0)

  # To insert card into the deck
  def insert_card(self, card, position):
    self.cards.insert(position, card)

  # To peek top 3 cards on top of the deck
  def show_top3_cards(self):
    i=0
    while i < len(self.cards) and i <= 2 :
      print(self.cards[i].name)
      i+=1

# Players class
class Player:

  # Initialization player with their name and hand(cards with them)
  def __init__(self, name):
    self.name = name
    self.hand = []

  # To print the cards for that player
  def print_hand(self):
    for i in range(len(self.hand)):
      print("index -" , i, ":", self.hand[i].name)
    return

  # To insert card to that particular players hand
  def add_card(self, card):
    self.hand.append(card)
    return

  # To draw card from deck and insert to particular players hand
  def draw_card(self, deck):
    card = deck.draw_card()
    self.hand.append(card)
    return card

  # To drop card from that players hand
  def play_card(self, card):
    for c in self.hand:
      if c.name == card.name:
        self.hand.remove(c)
        return

  # If exploding kitten is drawn
  def has_exploding_kitten(self):
    for card in self.hand:
      if card.name == 'Exploding Kitten':
        return True
    return False

  # To remove card from the hand
  def remove_card(self, card):
    for c in self.hand:
      if c.name == card.name:
        self.hand.remove(c)
        return

  # Defuse card implementation
  def has_defuse(self):
    for card in self.hand:
      if card.name == 'Defuse':
        return True
    return False

  # check for another similar cat card in hand
  def has_another_cat_card(self, name):
    for card in self.hand:
      if card.name==name:
        return True
    return False

  # drop defuse with exploding kitten card
  def defuse_exploding_kitten(self, deck, position):
    if self.has_defuse():
      self.remove_card(Card('Defuse'))
      self.remove_card(Card('Exploding Kitten'))
      deck.insert_card(Card('Exploding Kitten'), position)
      return True
    return False

# Start the game
class Game:
  def __init__(self, num_players):
    self.deck = Deck(num_players)
    self.players = []
    for i in range(num_players):
      self.players.append(Player('Player'+str(i+1)))
    self.deck.create_initial_deck()
    self.deck.shuffle_deck()
    self.distribute_cards()
    self.deck.add_remaining_cards()
    self.deck.shuffle_deck()
    self.current_player_index = 0
    self.played_skip = False
    self.attack_num = 0
    self.attack_mode = False
    self.played_attack = False
    self.play = "Y"

  # Distribute first round of cards.
  def distribute_cards(self):
    num_cards_per_player = 7
    for i in range(num_cards_per_player+1):
      for player in self.players:
        if i==0:
          player.add_card(Card('Defuse'))
        else:
          player.draw_card(self.deck)
          
    # Shuffle cards randomly
  def shuffle_card_action(self):
    self.deck.shuffle_deck()
    print("The deck has been shuffled.")
    
    # See the top 3 cards from deck 
  def see_the_future_card_action(self):
    print("You played 'See The Future' card.")
    print("Here are the top three cards of the deck: ")
    self.deck.show_top3_cards()

  # When playing "2 cats of same kind" or "favor" card, the
  # current player has to choose from the rest of the players
  # from whom they want to take a card from.
  def choose_player_to_take_card_from(self, current_player):
    print("Here are the other player names:")
    valid_indicies = []
    for i in range(len(self.players)):
      if self.players[i].name!=current_player.name:
        valid_indicies.append(i)
        print("index -", i, self.players[i].name)

    # Prompt user for a valid player index.
    while True:
      player_other_index = int(input("Enter the index of the player choose card from: "))
      if player_other_index not in valid_indicies:
        print("Sorry, your index is invalid. Please choose one of", valid_indicies)
        continue
      else:
        break

    player_other = self.players[player_other_index]
    return player_other

    # Favor card implementation
  def favor_card_action(self, current_player):
    # Choose which player you want to ask to give you a card.
    player_other = self.choose_player_to_take_card_from(current_player)


    # Ask the other player to pick the card they want to give away.
    print(player_other.name, "Here are your cards:")
    player_other.print_hand()

    # Prompt the user until they give a valid index of the card they want to give away.
    while True:
      card_index = int(input("Enter the index of the card you want to give away: "))
      if card_index not in range(len(player_other.hand)):
        print("Sorry, your index is invalid. Please choose an index between [", 0, len(player_other.hand)-1, "]")
        continue
      else:
        break

    picked_card = Card(player_other.hand[card_index].name)

    # Remove the picked card from teh other player
    # and add it to the current player.
    current_player.add_card(picked_card)
    player_other.remove_card(picked_card)

    print(current_player.name, "The card",picked_card.name, "from", player_other.name, "has been added to your hand.")

  def defuse_card_action(self):
    print("You have played a defuse card without an exploding kitten. Your defuse card is wasted.")
    
    # Skip card 
  def skip_card_action(self):
    # If a skip card is played, reduce attack_num by 1.
    # This will take care of the skip card action if the player is under attack.
    self.attack_num -= 1
    # This flag will ensure that the player does not need to draw a card later
    # if the skip is played (while taking care of attack card.)
    self.played_skip = True
    print("You played a Skip card, you will not be asked to draw a card unless you are attacked.")

  def attack_card_action(self):
    # Whenever an attack card is played, the attack_num is increased by 2. This
    # will also handle the condition when the attack is played on an attack.
    self.attack_num += 2
    self.played_attack = True
    print("You played an Attack card, you will not be asked to draw a card.")

  def choose_random_card_from_player(self, player_other):
    # Ask the current player which card he wants to choose from the other player.
    # This function is used by two_cat_card_action because the player will have the chance to
    # choose a random card from any single plater
    print("The chosen player", player_other.name," has cards from index", 0,"to", len(player_other.hand)-1)

    while True:
      card_index =int(input("Enter the random index of the card you want to pick: "))
      if card_index not in range(len(player_other.hand)):
        print("Sorry, your index is invalid. Please choose an index between [", 0, len(player_other.hand)-1, "]")
        continue
      else:
        break

    picked_card = Card(player_other.hand[card_index].name)

    return picked_card


  def cat_card_action(self, current_player, played_card):
    #Check if the player has two cards of the same cat card that is played.
    has_two = current_player.has_another_cat_card(played_card.name)
    # If the player plays a cat card, we prompt them to see if they want to play
    # another cat card of the same kind. This will take care of the case where
    # the current player can pick a random card from any single player.
    if has_two:
      valid_responses = ["Y", "N"]
      while True:
        another_card = input("Will you play another similar cat_card(Enter 'Y' or 'N'): ")
        if another_card not in valid_responses:
          print("Sorry, your response is incorrect. Please try again.")
          continue
        else:
          break

      if another_card == 'Y':
        # Play the other cat card as well.
        current_player.play_card(played_card)

        # Choose which layer you want to take card from.
        player_other = self.choose_player_to_take_card_from(current_player)

        # Choose the index of the card they want to pick from.
        picked_card = self.choose_random_card_from_player(player_other)

        # Remove the chosen card from other player
        # and add it to the current player.
        current_player.add_card(picked_card)
        player_other.remove_card(picked_card)

        print(current_player.name, "The card",picked_card.name, "from", player_other.name, "has been added to your hand.")

  # Calls relevent function according to card played.
  def action_card(self, played_card, current_player):
    if played_card.name in self.deck.cat_cards:
      self.cat_card_action(current_player, played_card)

    if played_card.name == "Shuffle":
      self.shuffle_card_action()

    if played_card.name == "Favor":
      self.favor_card_action(current_player)

    if played_card.name == "See The Future":
      self.see_the_future_card_action()

    if played_card.name == 'Skip':
      self.skip_card_action()

    if played_card.name == 'Attack':
      self.attack_card_action()

    if played_card.name == "Defuse":
      self.defuse_card_action()

  # Helper function for a player to defuse exploding kitten card.
  def player_defuse_exploding_kitten(self, current_player):
    while True:
      pos = int(input("Enter the index you want to insert the exploding kitten back in the deck: "))
      if pos not in range(len(self.deck.cards)):
        print("Sorry, your index is invalid. Please choose an index between [", 0, len(self.deck.cards)-1, "]")
        continue
      else:
        break
    current_player.defuse_exploding_kitten(self.deck, pos)

  def action_exploding_kitten(self, current_player):
    print(current_player.name,"-")
    has_defuse_card = current_player.has_defuse()
    # If the player does not have defuse card, they lose.
    # We force the player to defuse the exploding if they have
    # the defuse card, because otherwise, they lose the game.
    if not has_defuse_card:
      print("You do not have a defuse card. Your game ends now.")
      self.players.remove(current_player)
      return "End"
    else:
      print("Your only option to be in the game is to diffuse the exploding kitten.")
      print("Currently the deck has cards from index 0 to index", len(self.deck.cards) - 1)
      print(current_player.name,"-")
      self.player_defuse_exploding_kitten(current_player)
      return "Continue"

  # This is helper function used by player_draws_card
  # and action if the card drawn is an exploding kitten.
  def player_draw_card(self, current_player):
    new_card = current_player.draw_card(self.deck)
    print(current_player.name, "You drew the card", new_card.name)
    if new_card.name == "Exploding Kitten":
      ans = self.action_exploding_kitten(current_player)
      return ans
    return "Continue"

  # This function implememts how many times a player should draw card.
  # --> If they are in attack mode and did not attack card themseleves, the
  #     player draws the card "attack_num" times. This count "attack_num" is
  #     calculated based on a few factors like, if the current player is double
  #     attacked or if the current player played a skip card.
  # --> If the player is not under attack, it prompts the user to draw a card
  #     only if they have not played a skip card.

  # # attack mode
  #   played attack -- no need to draw
  #   played skip -- may be draw card
  #   not played skip - may be draw card
  #   not played attack - may be draw card
  # # not attack mode
  #   played attack - no need to draw
  #   played skip - no need to draw
  #   not played skip - draw
  #   not played attack - draw
  def player_draws_card(self, current_player):
    if self.attack_mode:
      if not self.played_attack:
        print("You are in attack mode, you need pick card", self.attack_num, "time(s).")
        if self.played_skip:
          print("Because you also played skip card(s).")
        for i in range(self.attack_num):
          exploded = self.player_draw_card(current_player)
          if exploded == "End":
            break
    elif not self.played_attack and not self.played_skip:
      print("You are not in attack mode, neither did you play skip, so you need to draw a card.")
      self.player_draw_card(current_player)

  def prompt_for_card_index(self, current_player):
    while True:
      index = int(input("Enter the index of the card you want to play: "))
      if index not in range(len(current_player.hand)):
        print("Sorry, your index is not valid. Please try again.")
        continue
      else:
        break
    played_card = current_player.hand[index]
    current_player.play_card(played_card)

    return played_card

  # Helper function used by player_plays_cards
  # to ask if a player wants to play card or not.
  def prompt_if_want_to_play(self, current_player):
    print(current_player.name, "Here are your cards:")
    current_player.print_hand()

    valid_responses= ["Y", "N"]
    while True:
      self.play = input("Enter 'Y' to play card or 'N' to pass: ")
      if self.play not in valid_responses:
        print("Sorry, your response is incorrect. Please try again.")
        continue
      else:
        break

  # Runs in a loop prompiting the current player to choose
  # if they want to play card.
  def player_plays_cards(self, current_player):
    # Each player can play any number of cards in each turn and therefore
    # this loop runs until the current player wants to stop playing.
    while self.play=='Y':
      # Ask player to play card.
      self.prompt_if_want_to_play(current_player)
      if self.play=='N':
        break

      played_card = self.prompt_for_card_index(current_player)
      self.action_card(played_card, current_player)

  # Helper function to reset certain flags after the end of each
  # player's turn.
  def end_of_turn_actions(self):
    if self.played_attack:
      print("Next player is under attack.")
      self.attack_mode = True
    else:
      self.attack_mode = False
      self.attack_num = 0

    self.play = "Y"
    self.played_skip = False
    self.played_attack = False
    self.current_player_index = (self.current_player_index + 1) % len(self.players)

  # Call this fuction to start the game.
  def play_game(self):
    # Main game loop
    # The loop runs until only player stands.
    while len(self.players)>1:
      # Get the current player
      current_player = self.players[self.current_player_index]
      print("This is now ", current_player.name, "turn.")
      print("You will be continuously asked to play card until you wish to stop. Your turn in most cases ends by drawing a card.")

      # Play cards
      self.player_plays_cards(current_player)

      # Draw card
      self.player_draws_card(current_player)

      # Reset flags.
      self.end_of_turn_actions()

    # End of the game.
    print("The game ends now.")
    print(self.players[0].name, "is the winner. Congratulations!")

## Drivers code - Main Program
print("Welcome to the Exploding Kittens Game")
print("This game can be played by 2 to 5 players")
number_of_players = 2
while True:
  number_of_players = int(input("Number of players who wish to play the game: "))
  if number_of_players not in range(2,6):
    print("Sorry, the number of players should be between 2 and 5. Please try again.")
    continue
  else:
    break
game = Game(number_of_players)
game.play_game()

