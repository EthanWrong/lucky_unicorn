"""Lucky Unicorns (LU) base component
Components added after they have been created and tested"""


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
    print("<program continues>")


# function to get user balance
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


played_before = yes_no("Have you played Lucky Unicorns before? ")

if played_before == "No":
    instructions()
else:
    print("<program continues>")

# gets user balance
user_balance = get_user_balance(1, 10)
print(f"${user_balance}, <program continues>")

