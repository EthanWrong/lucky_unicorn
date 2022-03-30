"""Component 2 (get_user_balance (how much)) v2
Changed function name from 'how_much' to 'get_user_balance' for better
readability
Took the code from v1 and cleaned it up to make the code nicer and the
usability/aesthetics cleaner. Also removed hardcode, and replaced it with
variables."""


def get_user_balance(minimum, maximum):
    balance = 0  # this means the minimum value cannot be 0 or lower

    # keep asking until a valid amount is entered
    while not minimum <= balance <= maximum:

        try:
            # this asks the user for an amount
            balance = int(input("How much money would you like to play with?"
                                " "))

        # if the input is not an integer, it will ask for another number
        except ValueError:
            print(f"That is an invalid number. Please enter a number between "
                  f"{minimum} and {maximum}.")
        # once the user has been asked for an amount, and it is definitely
        # an integer, it will test if it is a valid amount
        else:
            if not minimum <= balance <= maximum:
                print(f"That is an invalid amount. Please enter a number "
                      f"between {minimum} and {maximum}.")
        print()
    # once a valid amount has been found, the int amount will be returned
    return balance


# main routine
user_balance = get_user_balance(1, 10)
print(f"${user_balance}, <program continues>")
