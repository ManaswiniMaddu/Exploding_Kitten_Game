# Exploding_Kitten_Game
This project implements a simplified version of the popular card game Exploding Kittens using Python and object-oriented programming. The game supports 2 to 5 players, with essential game mechanics like drawing cards, playing action cards, and avoiding Exploding Kittens!

# Overview
In this strategic game, players draw cards, play actions, and try to avoid "exploding." The last player who hasn’t drawn an Exploding Kitten card wins.

# Setup
Initial Deck Composition:
1. Action Cards:
4 ATTACK cards, 4 SHUFFLE cards, 4 SKIP cards, 5 SEE THE FUTURE cards
CAT cards: TacoCat, Beard Cat, Rainbow-Ralphing Cat, Cattermelon, Hairy Potato Cat
2. Special Cards:
DEFUSE: 2 DEFUSE cards for 2-3 players, or 6 DEFUSE cards for 4-5 players
EXPLODING KITTEN: (Number of players - 1) cards used.
Each player receives 7 random cards from the initial deck and 1 DEFUSE card. The remaining DEFUSE and EXPLODING KITTEN cards are shuffled back into the deck.

# Game Rules
1. Turn Sequence:
Each player may play any number of action cards on their turn.
The turn ends with drawing a card from the deck.
If a player draws an EXPLODING KITTEN and lacks a DEFUSE card, they lose.
2. End Condition: The game continues until one player remains, who is declared the winner.

# Action Card Rules
SHUFFLE: Randomly shuffles the deck.
SEE THE FUTURE: View the top 3 cards of the deck privately.
CAT CARDS: Playing a matching pair allows you to steal a random card from another player.
FAVOR: Choose a player who must give you a card of their choice.
ATTACK: Skip your turn and force the next player to take two turns.
SKIP: End your turn without drawing a card.
EXPLODING KITTEN: If drawn, this must be revealed immediately. You lose if you don’t have a DEFUSE card.
DEFUSE: Allows you to place an EXPLODING KITTEN card back into the deck at any position.

# Project Structure
Key Classes
Card: Represents individual cards in the game.
Deck: Manages the deck, including shuffling and drawing.
Player: Represents each player, managing their hand and actions.
Game: Controls the overall game flow and player interactions.

# Features
Supports 2 to 5 players
Implements core game mechanics and special actions
Follows object-oriented programming principles
Includes an interactive command-line interface for gameplay

# Steps to Create
It is written in Python and it needs Python 3.x to test this game working.
1. Define the main classes
2. Implement game setup
3. Implement game logic
4. Create a user interface
   
# How to Play
Run the Python script.
Enter the number of players (2-5).
Follow the on-screen prompts to play action cards, draw from the deck, and interact with other players.
The last player remaining wins the game.

Requirements: Python 3.x

