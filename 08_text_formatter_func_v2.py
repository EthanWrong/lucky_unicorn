"""This code will format any string to add decoration to it and make it
stand out more.
Taken from v1, this code adds indenting"""
import math


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

format_decorate("-", 40, "Welcome to the Lucky Unicorn Game")
print()
format_decorate("#", 28, "Unicorn", 2)
print()
format_decorate("*", 9, "Goodbye")
print()
format_decorate("@", 8, "Hello World")
print()
format_decorate("=", 7, "Welcome")
print()
