"""This code will pick a random item from a string, all items in the string
having an equal chance of being picked"""

import random


def generate_token(tokens):
    for i in range(1, 11):
        token_choice = random.choice(tokens)
        print(f"{i} - {token_choice}")


# main routine
tokens = ("unicorn", "horse", "horse", "donkey", "donkey", "zebra", "zebra")
generate_token(tokens)
