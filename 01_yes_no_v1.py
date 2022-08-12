# using a while loop, ask users if they had played before until they type quit to exit
played_before = ""
while played_before != "quit":

    # ask the user of they have played before
    played_before = input("Have you play this game before? ").lower()

    # if they say yes or y, output program continues
    if played_before == "yes":
        print("Program continues")

    elif played_before == "y":
        print("Program continues")

    # if they say no or n, output 'Show instructions
    elif played_before == "no":
        print("Show instructions")

    elif played_before == "n":
        print("Show instructions")

    # if quit, exit the game
    # if other, print error
    elif played_before == "quit":
        print("Game exit")
    else:
        print("Please answer yes / no")
