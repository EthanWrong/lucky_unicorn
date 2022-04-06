"""Code copied from v1, but the chances of each token are changed with the
tuple picking method. Also added code that makes it easier to read losses.
"""
import random


def play_round(user_balance):
    if user_balance > 0:
        user_balance = calc_balance(user_balance)
        return user_balance
    else:
        print("You are out of money, sorry.")


def calc_balance(current_balance):
    winnings = generate_token()
    new_balance = float(current_balance + winnings - 1)
    print(f"Current Balance: ${new_balance:.2f}")
    return new_balance


def generate_token():
    tokens = ("unicorn",
              "zebra", "zebra", "zebra", "zebra",
              "horse", "horse", "horse", "horse",
              "donkey", "donkey", "donkey", "donkey")
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
user_balance = 100.0

for i in range(1, 21):
    user_balance = play_round(user_balance)

print(f"\nEnd Balance: ${user_balance}\nLost ${100.0-user_balance}")
