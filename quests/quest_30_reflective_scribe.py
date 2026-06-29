#!/usr/bin/python3
# Quest 30: The Reflective Scribe
#
# Task: Go back to three previous assignments and add comments
#       (# like this) to explain what each part of the code does and why.
#
# ─────────────────────────────────────────────────────────────────────────────
# The three quests chosen for annotation and the reasoning behind each:
# ─────────────────────────────────────────────────────────────────────────────
#
# 1. quest_25_number_wizard.py
#    WHY: The while True / break pattern is a common Python idiom that isn't
#    obvious at first glance. Comments explain why 'break' is the exit
#    condition instead of a normal while condition, and why directional
#    feedback ("too high / too low") is more useful than a plain "wrong".
#
# 2. quest_26_simple_calculator.py
#    WHY: This script uses functions for the first time alongside an
#    if/elif chain. Comments explain the design choice of separating each
#    operation into its own function (modularity), why float() is used
#    instead of int() (to handle decimals), and why divide() checks for
#    zero before doing the calculation (to prevent a crash).
#
# 3. quest_27_fizzbuzz.py
#    WHY: FizzBuzz has a subtle ordering trap — checking the single
#    conditions before the combined condition causes bugs. Comments
#    explain why the 'both' check must come first, and what the modulo
#    operator (%) actually does, since it's a new concept in this quest.
#
# ─────────────────────────────────────────────────────────────────────────────
# All three files have been updated directly in the quests/ folder.
# ─────────────────────────────────────────────────────────────────────────────

print("Quest 30: The Reflective Scribe")
print()
print("Three previous quests have been annotated with comments:")
print("  → quest_25_number_wizard.py  (while/break pattern + feedback logic)")
print("  → quest_26_simple_calculator.py (functions, float(), zero-division guard)")
print("  → quest_27_fizzbuzz.py       (modulo operator + ordering of conditions)")
print()
print("Open any of those files to read the explanations.")
