# function goes here
def yes_no(question):
    valid = False
    while not valid:
        # Ask the user of they have played before
        response = input(question).lower()

        # If they say yes, output program continues
        if response == "yes" or response == "y":
            recap_instruction = input("Do you need a recap of the instructions?    ").lower()
            if recap_instruction == "yes" or recap_instruction == "y":
                response = "show instructions"
                return response
            if recap_instruction == "no" or recap_instruction == "no":
                response = "continue program"
                # if they say yes, return yes
                return response

        # If they say no, output 'Show instructions
        elif response == "no" or response == "n":
            response = "Show instructions"
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
print("You have chosen to {}".format(played_before))
