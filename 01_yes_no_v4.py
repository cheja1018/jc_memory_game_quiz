# function goes here
def yes_no(question):
    valid = False
    while not valid:
        # Ask the user of they have played before
        response = input(question).lower()

        # If they say yes, output program continues
        if response == "yes" or response == "y":
            response = "continue program"
            # if they say yes, return yes
            return response

        # If they say no, output 'Show instructions
        elif response == "no" or response == "n":
            response = "show instructions"
            # if they say no, return no
            return response

        # If other, print error
        elif response == "quit":
            response = "to quit"
            # if they say no, return no
            return response
        else:
            print("Please answer yes / no")


# main routine goes here...
played_before = yes_no("Have you play this game before?   ")
print()

# ask if they need a reminder of the instructions
if played_before == "continue program":
    played_before = yes_no("Do you remember how to play?   ")

print("You have chosen to {}".format(played_before))
