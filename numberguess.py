import random


class NumberGuess:

    def __init__(self):
        self.score = 0
        self.gm = input('MODE [easy, medium, hard]>: ')

    def start(self):
        while True:
            try:
                if self.gm.lower() == 'easy':
                    attempt = 5
                    x = random.randint(1, 5)
                    y = random.randint(5, 10)
                elif self.gm.lower() == 'medium':
                    attempt = 5
                    x = random.randint(1, 5)
                    y = random.randint(10, 20)
                elif self.gm.lower() == 'hard':
                    attempt = random.randint(1, 5)
                    x = random.randint(1, 5)
                    y = random.randint(10, 25)
                range_of_xy = random.randint(x, y)

                print(f'Guess the number between {x} and {y} ')
                while True:
                    print(f'You\'ve got {attempt} more attempt(-s)')
                    answer = input('>: ')
                    if answer == 'exit':
                        exit()
                    try:
                        if int(answer) < range_of_xy:
                            print('Your answer is lower than the number')
                            attempt -= 1
                            print(f'Attempts left: {attempt}')
                        elif int(answer) > range_of_xy:
                            print('Your answer is higher than the number')
                            attempt -= 1
                            print(f'Attempts left: {attempt}')
                        elif int(answer) == range_of_xy:
                            print('You guessed the number! Good job!')
                            self.score += 1
                            print(f'Your score is: {self.score}')
                            break
                        elif answer == 'exit':
                            exit()
                        if attempt == 0:
                            print('Sorry, no more attempts.')
                            self.score -= 1
                            print(f'Your score: {self.score}')
                            break
                    except ValueError:
                        print('Something went wrong. Make sure you type numbers or "exit"')
            except KeyboardInterrupt:
                exit()
