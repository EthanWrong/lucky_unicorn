"""Lucky Unicorns (LU) base component v2
Components added after they have been created and tested
Added text formatter to many prints:
  > For generate token, made a new if() statement for each token
"""
import random
import math


# yes/no checking function, will return capitalized 'Yes' or 'No'
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, output 'Program Continues'
        if answer in ("yes", "y"):
            answer = "Yes"
            return answer

        # If they say no, output 'Display instructions'
        elif answer in ("no", "n"):
            answer = "No"
            return answer

        # Otherwise, show error
        else:
            print("Please answer 'yes' or 'no'")


# function to display instructions
def instructions():
    print("**** How to Play ****")
    print()
    print("The rules of the game will go here")
    print()


# function to get user balance
def get_user_balance(minimum, maximum):
    balance = 0  # this means the minimum value cannot be 0 or lower

    # keep asking until a valid amount is entered
    while not minimum <= balance <= maximum:

        try:
            # this asks the user for an amount
            balance = int(input("How much money would you like to play with >>"
                                "> "))

        # if the input is not an integer, it will ask for another number
        except ValueError:
            print(f"That is an invalid number.\n Please enter a number "
                  f"between "
                  f"{minimum} and {maximum}.")
        # once the user has been asked for an amount, and it is definitely
        # an integer, it will test if it is a valid amount
        else:
            if not minimum <= balance <= maximum:
                print(f"That is an invalid amount.\n Please enter a number "
                      f"between {minimum} and {maximum}.")
        print("=====")
    # once a valid amount has been found, the int amount will be returned
    print(f" = wallet = ${balance:.2f}\n")
    return balance


def play_round(balance):
    if balance > 0:
        balance = calc_balance(balance)
        return balance
    else:
        print("You are out of money, sorry.")


def calc_balance(current_balance):
    winnings = generate_token()
    new_balance = float(current_balance + winnings - 1)
    print(f"\n = wallet = ${new_balance:.2f}\n")
    return new_balance


def generate_token():
    number = random.randint(1, 100)
    if 1 <= number <= 50:
        token_choice = random.choice(("zebra", "horse"))
        format_decorate(":", 28, token_choice)
        format_decorate(":", 28, "+ $0.50")

    elif 51 <= number <= 93:
        token_choice = "donkey"
        format_decorate(".", 28, token_choice)
        format_decorate(".", 28, "+ $0.00")

    else:
        token_choice = "unicorn"
        format_decorate("#", 28, token_choice)
        format_decorate("#", 28, "+ $5.00")

    # calculates winnings
    if token_choice == "donkey":
        winnings = 0.00
    elif token_choice in ("zebra", "horse"):
        winnings = 0.50
    elif token_choice == "unicorn":
        winnings = 5.00

    return winnings


# IMPORTANT! check that: width >= len(text) + 2
def format_decorate(decoration, width, text, indent=0):
    if width < len(text) + 2:  # checks that the text can actually be decorated
        print("<error: width of statement too large>")

    else:
        indent = " " * indent
        top_bottom_row = f"{indent}{decoration * width}"

        # subtracts 2 spaces and text length from the total width
        side_length = (width - (len(text) + 2)) / 2

        left_side = (math.floor(side_length)) * decoration
        right_side = (math.ceil(side_length)) * decoration

        inner_row = f"{indent}{left_side} {text} {right_side}"

        print(top_bottom_row)
        print(inner_row)
        print(top_bottom_row)


# main routine

format_decorate("=", 41, "Welcome to the Lucky Unicorn Game")
played_before = yes_no("Have you played Lucky Unicorns before >>> ")

if played_before == "No":
    instructions()


# gets user balance
user_balance = get_user_balance(1, 10)


# play game (looping + mechanics)
while user_balance >= 1:
    confirm_play_round = yes_no("Play a round ($1.00) >>> ")
    if confirm_play_round == "Yes":
        user_balance = play_round(user_balance)
    else:
        format_decorate("-", 40, "Betting finished")
        format_decorate("+", 40, f"Your final balance was ${user_balance:.2f}")
        print("=============== Goodbye ================")
        break


