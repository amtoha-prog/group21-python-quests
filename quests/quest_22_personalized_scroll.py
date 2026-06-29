def personalized_greeting(name, quest):

    print()
    print(f"Brave adventurer {name} has taken up the quest to {quest}!")
    print(f" Salutes you, {name}. May it work out")

    adventurer_name = input("Enter your hero's name: ")
    adventurer_quest = input("Enter your quest: ")

    personalized_greeting(adventurer_name, adventurer_quest)
