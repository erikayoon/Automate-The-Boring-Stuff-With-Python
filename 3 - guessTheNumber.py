# Modified Version of the "Guess The Number" Game in Chapter 3

import random

num = random.randint(1,20) # Generate a random number
guess = 0
counter = 0

print('I am thinking of a number between 1 and 20.')
while int(guess) != num:
    print('Take a guess')
    guess = input()
    counter = counter + 1 # Counts how many times the user has made a guess

    # Try and Except statement to validate whether input is of correct format
    try:
        if int(guess) == num:
            print('Good job! You guessed my number in ' + str(counter) + ' guesses!')
        elif int(guess) > num and int(guess) <= 20:
            print('Your guess is too high')
        elif int(guess) < num and int(guess) >= 1:
            print('Your guess is too low')
        else:
            print('Your guess is out of range. Please try again.')
            
    except ValueError:
        print('Guess must be an integer. Please try again.')
        guess = 0