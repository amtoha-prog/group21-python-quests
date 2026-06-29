direction = input("Do you go left or right? ").lower()
if direction == "left":
    action = input("Do you swim or wait? ").lower()
    if action == "swim":
        print("You found a treasure chest! You win!")
    else:
        print("You waited too long. The path closed.")
else:
    print("You walked right into a dead end.")
