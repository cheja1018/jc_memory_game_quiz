# function goes here
def yes_no(question):
    valid = False
    while not valid:
        # Ask the user of they have played before
        response = input(question).lower()

        # If they say yes, output program continues
        if response == "yes" or response == "y":
            print()
            response = "continue program"
            # if they say yes, return yes
            return response

        # If they say no, output 'Show instructions
        elif response == "no" or response == "n":
            print()
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


# instructions in a function, basic rules
def instructions():
    # title
    print("How To Play")
    print()
    # the rules
    print("To play, the computer would generate a random 8 digit number.\n"
          "After 10 seconds, the the 8 digit number would disappear.\n"
          "You will need to type out the 8 digit code.\n"
          "If you get it correct the game continues, if not you will lose one of your lives.\n"
          "You'll have a total of 3 lives, once they run out the game ends\n"
          "If you want to quit the game press <esc>")
    return ""


# main routine goes here...
played_before = yes_no("Have you play this game before?   ")
print()

# ask if they need a reminder of the instructions
if played_before == "continue program":
    played_before = yes_no("Do you remember how to play?   ")

# when users need instructions display them
if played_before == "show instructions":
    instructions()
