"""LU yes / no

"""
show_instructions = ""
while not show_instructions in ("yes", "y", "no", "n"):
    # Ask the user if they have played before
    name = "Lucky Unicorns"
    show_instructions = input(f"Have you played {name} before >>> ").lower()

    # If they say yes, output 'Program Continues'
    if show_instructions in ("yes", "y"):
        print("Program continues")

    # If they say no, output 'Display instructions'
    elif show_instructions in ("no", "n"):
        print("Display instructions")

    # Otherwise, show error
    else:
        print("Please answer 'yes' or 'no'")

    print(f"You entered '{show_instructions}'")
