import random


class Dice:

    @staticmethod
    def start():
        while True:
            dice = random.randint(1, 6)
            try:
                print(f'The dice landed on {dice}')
                print('Would you like to throw again? (yes/no)')
                action = input('>: ')
                if action.lower() == 'yes':
                    pass
                elif action.lower() == 'no':
                    print('Farewell wanderer.')
                    exit()
                else:
                    pass
            except KeyboardInterrupt:
                print('Goodbye.')
                exit()
