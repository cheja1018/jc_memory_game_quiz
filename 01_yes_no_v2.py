# using a while loop, ask users if they had played before until they type quit to exit
played_before = ""
while played_before != "quit":

    # ask the user of they have played before
    played_before = input("Have you play this game before? ").lower()

    # if they say yes or y, output program continues
    if played_before == "yes" or played_before == "y":
        # ask users if they still need instructions
        recap_instruction = input("Do you need a recap of the instructions?    ").lower()
        # if yes, show instructions
        if recap_instruction == "yes" or recap_instruction == "y":
            print("Show instructions")
        # if no, program continues
        if recap_instruction == "no" or recap_instruction == "no":
            print("program continues")

    # if they say no, output Show instructions
    elif played_before == "no" or played_before == "n":
        print("Show instructions")

    # if users type quit, game exits
    elif played_before == "quit":
        print("Game exit")
    # if other, print error
    else:
        print("Please answer yes / no")
