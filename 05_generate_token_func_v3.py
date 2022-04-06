"""This is copied from v2 but the method for picking a token is different.
This method uses a number generator."""

import random


def generate_token():
    number = random.randint(1, 100)
    if 1 <= number <= 70:
        token_choice = random.choice(("zebra", "horse"))
    elif 71 <= number <= 99:
        token_choice = "donkey"
    else:
        token_choice = "unicorn"
    print(token_choice)

    # calculates winnings
    if token_choice == "donkey":
        winnings = 0.00
    elif token_choice in ("zebra", "horse"):
        winnings = 0.50
    elif token_choice == "unicorn":
        winnings = 5.00

    return winnings


# main routine


# tests
print("Test 1:")
print(f"${generate_token():.2f}\n")
print("\nTest 2:")
for i in range (1, 11):
    print(f"${generate_token():.2f}\n")
