"""LU yes / no
bases on 01_yes_no_v3
"""


# Functions go here...
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


# Main routine go here...


show_instructions = yes_no("Have you played Lucky Unicorns before? ")
print(f"You entered '{show_instructions}'")
print()
having_fun = yes_no("Are you having fun? ")
print(f"You entered '{having_fun}'")



