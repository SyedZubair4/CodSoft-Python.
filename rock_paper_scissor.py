import random

# Defining variables
loose = 0
win = 0
tie = 0

print('If you want to quit the game, then just type "quit"')
options = ['rock', 'paper', 'scissor']

while True:
    cho = input('Its your turn choose one among them\nrock,paper,scissor,quit\n')

    # Checking for valid input
    if cho not in options and cho != 'quit':
        print('Invalid input. Please choose from rock, paper, or scissor.')
        continue
    # taking computer choice
    comp_cho = random.choice(options)

    # Check for quit
    if cho == 'quit':
        break

    print('You choose ' + str(cho) + '\nComputer choose', comp_cho)

    # Determining the result
    if cho == comp_cho:
        print('It\'s a tie')
        tie += 1

    elif cho == 'rock':
        if comp_cho == 'paper':
            print('You Lost')
            loose += 1

        elif comp_cho == 'scissor':
            print('You Win')
            win += 1

    elif cho == 'paper':
        if comp_cho == 'rock':
            print('You Win')
            win += 1

        elif comp_cho == 'scissor':
            print('You Lost')
            loose += 1

    elif cho == 'scissor':
        if comp_cho == 'rock':
            print('You Lost')
            loose += 1

        elif comp_cho == 'paper':
            print('You Win')
            win += 1

# Displaying the results
print('Results.......\nWin=', win)
print('Loose=', loose)
print('Tie=', tie)
print('Thankyou for wasting your time')

