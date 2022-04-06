"""This code incorporates 05v2 and 06v1 to make a function that plays a round.
Generate tokens had the token tuple incorporated into it, making it a local
variable
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
    tokens = ("unicorn", "horse", "horse", "donkey", "donkey", "zebra", "zebra")
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
