"""Component 2 (how much) v1
Ask user how much money they want to play with. Checks to see if input is an
integer. If it is, it checks to see if input is a valid integer between 1
and 10. If it is, this amount becomes the balance in their account"""


def how_much():
    user_balance = 0

    # keep asking until a valid amount is entered
    while not 1 <= user_balance <= 10:

        try:
            # this asks the user for an amount
            user_balance = int(input("How much money would you like to play wi"
                                     "th? "))

        # if the input is not an integer, it will ask for another number
        except ValueError:
            print("That is an invalid number. Please enter a number "
                  "between 1 "
                  "and 10.")
        # once the user has been asked for an amount, and it is definitely
        # an integer, it will test if it is a valid amount
        else:
            if not 1 <= user_balance <= 10:
                print("That is an invalid amount. Please enter a number "
                      "between 1 and 10.")
    # once a valid amount has been found, the int amount will be returned
    return user_balance


# main routine
user_balance = how_much()
print(user_balance)
