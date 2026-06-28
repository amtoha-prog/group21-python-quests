#!/usr/bin/python3
# Quest 18: The Loop of Riddles
# Write a guessing game. Think of a secret number.
# Use a while loop to keep asking until they guess right.

secret = 42
guess = 0

while guess != secret:
    guess = int(input("Guess the secret number: "))
    if guess == secret:
        print("You got it! The secret number was 42!")
    else:
        print("Wrong! Try again.")
