#!/usr/bin/python3
# Quest 25: The Number Wizard
# The Quest: Upgrade your number guessing game. After each wrong guess,
# tell the user if their guess was "too high" or "too low".

import random

# Generate a random secret number between 1 and 100.
# random.randint is inclusive on both ends, so 1 and 100 are both possible.
secret_number = random.randint(1, 100)

print("Wellcome to the Number Wizard!")
print("I'm thinking of a number between 1 and 100")

# Keep looping until the player guesses correctly.
# 'while True' means the loop has no automatic end condition —
# it only stops when we explicitly call 'break' inside.
while True:
    # Ask the player for a guess and convert the text input to an integer
    # so we can compare it numerically against secret_number.
    guess = int(input("Enter your guess: "))

    # Compare the guess to the secret number and give directional feedback.
    # This tells the player which way to adjust, rather than just "wrong".
    if guess < secret_number:
        print("Too low, Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        # The guess exactly matches — congratulate the player and exit the loop.
        print("Congratulations!! You guessed the number.")
        break   # 'break' exits the while loop immediately
