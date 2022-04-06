"""Code copied from v2, but the token generator is taken from 05v3,
which means the token is generated with a random number system."""
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
user_balance = 100.0

for i in range(1, 21):
    user_balance = play_round(user_balance)

print(f"\nEnd Balance: ${user_balance}\nLost ${100.0-user_balance}")
