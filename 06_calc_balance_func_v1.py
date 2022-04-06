"""This code will subtract the given amount from user balance, and print the
user's balance"""


def generate_winnings():  # this will be replaced by <generate_token_func> in
    # final component
    winnings = 0.5
    print(f"Winnings = {winnings}")
    return winnings


def calc_balance(current_balance):
    winnings = generate_winnings()
    new_balance = float(current_balance + winnings - 1)
    print(f"Current Balance: ${new_balance:.2f}")
    return new_balance


# main routine
user_balance = 100.0
user_balance = calc_balance(user_balance)
user_balance = calc_balance(user_balance)  # testing repeats
