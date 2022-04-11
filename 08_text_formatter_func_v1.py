"""This code will format any string to add decoration to it and make it
stand out more"""
import math


# IMPORTANT! check that: width >= len(text) + 2
def format_decorate(decoration, width, text):
    if width < len(text) + 2:  # checks that the text can actually be decorated
        print("<error: width of statement too large>")

    else:
        top_bottom_row = decoration * width

        # subtracts 2 spaces and text length from the total width
        side_length = (width - (len(text) + 2)) / 2

        left_side = (math.floor(side_length)) * decoration
        right_side = (math.ceil(side_length)) * decoration

        inner_row = f"{left_side} {text} {right_side}"

        print(top_bottom_row)
        print(inner_row)
        print(top_bottom_row)


# main routine

format_decorate("-", 40, "Welcome to the Lucky Unicorn Game")
format_decorate("#", 28, "Unicorn")
format_decorate("*", 9, "Goodbye")
format_decorate("@", 8, "Hello World")
format_decorate("=", 7, "Welcome")
