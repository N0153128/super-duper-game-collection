import random


class WordGuess:

    def __init__(self):
        self.score = 0

    @staticmethod
    def separator(word):
        return [char for char in word]

    def start(self):
        with open('words', 'r') as file:
            bag = file.readlines()
            while True:
                try:
                    line = random.randint(1, 25)
                    theword = self.separator(bag[line].strip('\n'))
                    wrd = bag[line].strip('\n').lower()
                    amount = len(theword)
                    attempt = amount + 3
                    print(f'Total number of letters: {amount}, first letter is {theword[0]}')
                    print('Guess other letter')
                    while True:
                        uin = input('>: ')
                        if uin.lower() in theword:
                            print(f'Nice! There is {theword.count(uin.lower())} of letter {uin.lower()}')
                        elif uin.lower() == wrd:
                            print('You guessed the word!')
                            self.score += 1
                            print(f'Your score: {self.score}')
                            break
                        elif uin.lower() not in theword:
                            attempt -= 1
                            print(f'Missed! {attempt} attempts left')
                        if attempt == 0:
                            print('you lose')
                            break
                except KeyboardInterrupt:
                    print('Goodbye')
                    exit()
                except Exception as e:
                    print(e)
