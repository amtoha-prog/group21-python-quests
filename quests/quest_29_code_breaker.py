#!/usr/bin/python3
# Quest 29: The Code Breaker
# The user has 3 attempts to guess the secret code (42).
# After each wrong guess, feedback is given (too high / too low).
# The game ends immediately on a correct guess, or after 3 failed attempts.

SECRET_CODE = 42        # The secret code the user must crack
MAX_ATTEMPTS = 3        # Maximum number of guesses allowed

print("=" * 40)
print("   WELCOME TO THE CODE BREAKER")
print("=" * 40)
print("\nA secret code is hidden. You have 3 attempts.")
print("Crack it to win. Fail all three — the vault locks forever.\n")

# Track how many attempts the player has used
attempts_used = 0

# Loop runs until the player guesses correctly or uses all 3 attempts
while attempts_used < MAX_ATTEMPTS:

    # Calculate and display which attempt this is (e.g. "Attempt 1 of 3")
    attempt_number = attempts_used + 1
    print(f"Attempt {attempt_number} of {MAX_ATTEMPTS}:")

    # Get the player's guess and convert it to an integer
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        # Handle non-numeric input gracefully without burning an attempt
        print("  That's not a valid number. Try again.\n")
        continue

    # Check if the guess is correct
    if guess == SECRET_CODE:
        print(f"\n✅ CORRECT! The code was {SECRET_CODE}.")
        print("The vault swings open. You are a true Code Breaker!\n")
        break   # Stop the loop immediately — no more guesses needed

    # Guess is wrong — give directional feedback and count the attempt
    attempts_used += 1

    if guess < SECRET_CODE:
        print(f"  ❌ Too low! That's not it.\n")
    else:
        print(f"  ❌ Too high! That's not it.\n")

    # Warn the player if they have only one attempt remaining
    remaining = MAX_ATTEMPTS - attempts_used
    if remaining == 1:
        print("  ⚠️  Last chance — choose wisely!\n")

else:
    # This block runs only if the while loop exhausted all attempts
    # (i.e. the player never guessed correctly)
    print(f"🔒 LOCKED OUT. You used all {MAX_ATTEMPTS} attempts.")
    print(f"The secret code was {SECRET_CODE}. Better luck next time!\n")
