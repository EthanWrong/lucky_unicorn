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


# Main routine go here...


played_before = yes_no("Have you played Lucky Unicorns before? ")

if played_before == "No":
    instructions()
else:
    print("<program continues>")

