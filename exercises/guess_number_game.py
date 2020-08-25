from sys import argv
from random import randint

starting_number = int(argv[1])
ending_number = int(argv[2])

random_number = randint(starting_number, ending_number)
print(random_number)

while True:
    try:
        guessed_number = int(input('Please guess a number:\n'))
        if guessed_number == random_number:
            print(f'Correct! You guessed {guessed_number}, which was the same as {random_number}.')
            break
        elif guessed_number != random_number:
            print('Try again!')
            continue
    except ValueError:
        print('Please enter a number!')
        continue

