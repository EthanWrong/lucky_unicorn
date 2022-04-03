"""This code is taken from v1. Returns the winnings from each token
generated, and adds a test to see if it is random over 10 repeats."""

import random


def generate_token(tokens):
    token_choice = random.choice(tokens)
    print(f"{token_choice}")

    # calculates winnings
    if token_choice == "donkey":
        winnings = 0.00
    elif token_choice in ("zebra", "horse"):
        winnings = 0.50
    elif token_choice == "unicorn":
        winnings = 5.00

    return winnings


# main routine
tokens = ("unicorn", "horse", "horse", "donkey", "donkey", "zebra", "zebra")

# tests
print("Test 1:")
print(f"${generate_token(tokens):.2f}\n")
print("\nTest 2:")
for i in range (1, 11):
    print(f"${generate_token(tokens):.2f}\n")
