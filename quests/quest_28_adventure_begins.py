#!/usr/bin/python3
# Quest 28: The Adventure Begins
# A text-based Choose Your Own Adventure game.
# Functions handle each location. There are two different endings:
#   - The Hero's Victory (good ending)
#   - The Dragon's Triumph (bad ending)

def start():
    """The opening scene — the adventure begins here."""
    print("=" * 50)
    print("   THE QUEST FOR THE SUNSTONE")
    print("=" * 50)
    print("\nYou are a wandering adventurer standing at the")
    print("edge of the Whispering Forest. Legends say the")
    print("Sunstone — a gem of great power — lies somewhere")
    print("deep within.\n")

    print("A fork in the path lies before you:")
    print("  [1] Take the Dark Trail into the forest")
    print("  [2] Follow the river towards the old ruins")

    choice = input("\nWhat do you do? Enter 1 or 2: ").strip()

    if choice == "1":
        dark_trail()
    elif choice == "2":
        old_ruins()
    else:
        print("\nYou hesitate too long. A wolf chases you home. Game over.")


def dark_trail():
    """Location: The Dark Trail — a dense, eerie path through the forest."""
    print("\n--- THE DARK TRAIL ---")
    print("\nThe trees grow thick above you, blocking the moonlight.")
    print("You hear growling ahead. A large wolf blocks the path.")
    print("Next to the trail you spot a fallen branch and a bush")
    print("of bright berries — the wolf's favourite food.\n")

    print("What do you do?")
    print("  [1] Grab the branch and stand your ground")
    print("  [2] Toss the berries to distract the wolf")

    choice = input("\nYour choice: ").strip()

    if choice == "1":
        print("\nYou raise the branch boldly. The wolf snarls — then flees.")
        print("Your courage opens the way forward.")
        hidden_cave()
    elif choice == "2":
        print("\nThe wolf sniffs the berries eagerly and trots off the path.")
        print("Clever thinking! The trail is clear.")
        hidden_cave()
    else:
        print("\nYou freeze in fear. The wolf herds you back to the village.")
        print("Adventure over — better luck next time.")


def old_ruins():
    """Location: The Old Ruins — crumbling stone towers by the river."""
    print("\n--- THE OLD RUINS ---")
    print("\nCrumbled towers rise from the mist. Inside the largest")
    print("ruin you find an ancient inscription on the wall and")
    print("two staircases — one going up, one going down.\n")

    print("What do you do?")
    print("  [1] Climb the staircase going UP to the tower roof")
    print("  [2] Descend the staircase going DOWN into the vault")

    choice = input("\nYour choice: ").strip()

    if choice == "1":
        print("\nFrom the rooftop you spot a glowing light in the treetops —")
        print("it must be the Sunstone! You leap across to the trees.")
        hidden_cave()
    elif choice == "2":
        print("\nThe vault is flooded. You narrowly escape but lose your")
        print("gear. Exhausted, you return to the village to regroup.")
        print("\nYou survived — but the Sunstone remains hidden. Try again.")
    else:
        print("\nYou wander the ruins aimlessly until nightfall and turn back.")
        print("Adventure over.")


def hidden_cave():
    """Location: The Hidden Cave — the final challenge before the Sunstone."""
    print("\n--- THE HIDDEN CAVE ---")
    print("\nYou reach a cave entrance half-covered by vines.")
    print("Inside, a fierce dragon sleeps beside a glowing gem —")
    print("the Sunstone! Its chest rises and falls slowly.\n")

    print("You have one shot at this. What is your plan?")
    print("  [1] Sneak past the dragon and grab the Sunstone quietly")
    print("  [2] Challenge the dragon to battle for the gem")

    choice = input("\nYour choice: ").strip()

    if choice == "1":
        heroes_victory()
    elif choice == "2":
        dragons_triumph()
    else:
        print("\nYou back away slowly — and the dragon doesn't even wake up.")
        print("The Sunstone stays in the cave. Smart survival, at least.")


# ── ENDING 1 ──────────────────────────────────────────────────────────────────

def heroes_victory():
    """GOOD ENDING — The player successfully retrieves the Sunstone."""
    print("\n" + "=" * 50)
    print("   ENDING 1: THE HERO'S VICTORY")
    print("=" * 50)
    print("\nWith the grace of a shadow you creep across the cave floor.")
    print("Your fingers close around the warm, pulsing Sunstone.")
    print("The dragon shifts — you hold your breath — then it settles.")
    print("\nYou slip out of the cave and into the dawn light.")
    print("The kingdom rejoices. Songs are written in your honour.")
    print("\n*** CONGRATULATIONS — YOU WIN! ***\n")


# ── ENDING 2 ──────────────────────────────────────────────────────────────────

def dragons_triumph():
    """BAD ENDING — The dragon defeats the player in combat."""
    print("\n" + "=" * 50)
    print("   ENDING 2: THE DRAGON'S TRIUMPH")
    print("=" * 50)
    print("\n'WAKE AND FIGHT, BEAST!' you roar.")
    print("\nThe dragon's eyes snap open — twin furnaces of orange fire.")
    print("It rises to its full terrifying height, shaking the cave walls.")
    print("Your sword arm wavers. The dragon exhales one enormous flame.")
    print("\nYou are, very thoroughly, toast.")
    print("\n*** GAME OVER — The dragon wins this round. ***\n")
    print("Tip: Sometimes silence is the mightiest weapon.\n")


# ── Entry point ───────────────────────────────────────────────────────────────
start()
