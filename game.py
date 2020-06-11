from numberguess import NumberGuess
from dice import Dice
from hangman import WordGuess


print('Welcome to super-duper game collection! Type what game you would like to play.')
print('NUMBER GUESS \n DICE ROLLER \n WORD GUESS')
game = input('>: ')

if game.lower() == 'number guess':
    ng = NumberGuess()
    ng.start()
if game.lower() == 'dice roller':
    dice = Dice()
    dice.start()
if game.lower() == 'word guess':
    wg = WordGuess()
    wg.start()
