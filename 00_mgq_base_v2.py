"""
base component for my memory quiz game
V0 - skeleton setup
v1 - instructions and user yes no checker
v2 - created a number checker + input (changed to 03_num_gen_v3), created a loop (04_loop_v2) and timer (05_timer_v4)

author - Jasmine Chen
2022
"""

import random
from time import sleep


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
          "If you want to quit the game type \"quit\" when questions are asked.\n")
    return ""


# random generator, correct answer
def ran_gen():
    # modify lives out of scope
    global lives
    global rounds
    # try/except for all possible results, incase the input isn't an integer
    try:
        answer = input("What do you think the answer is ?   ")  # user input
        # comparing the user input to generated number
        if answer.lower() == "quit" or answer.lower() == "q" or lives == 0:
            print("Thanks for playing")
            exit("Game Exits")
            print()
            return
        answer = int(answer)
        if answer == num:
            print(correct)
            print()
            return answer
        elif answer != num:
            lives -= 1  # subtract one life if answered incorrectly
            print(incorrect, "the correct answer is {}".format(num))
            print()
            return answer

    # try/except for all possible results, incase the input isn't an integer
    except ValueError:
        print(error)
        print()


def enter_continue():
    input("Press Enter to continue...\n"
          "Timer of ten seconds would start straight away\n"
          "Good Luck!")
    print()


# main routine goes here...
played_before = yes_no("Have you play this game before?   ")
print()

# ask if they need a reminder of the instructions
if played_before == "continue program":
    played_before = yes_no("Do you remember how to play?   ")

# when users need instructions display them
if played_before == "show instructions":
    instructions()
    sleep(1)


# replies for correct and incorrect
correct = "That is correct, well done!"
incorrect = "Unfortunately, that is incorrect, you lose 1 life"
error = "That is not a number, please try again"

lives = 3
rounds = 0


# main routine goes here
# until lives reach 0, keep the loop going
while lives > 0:

    enter_continue()
    rounds += 1
    print("Round", rounds)
    print("You have a remainder of {} lives".format(lives))  # lives decrease each time it prints incorrect
    num = random.randrange(10000000, 99999999)  # number in ranges from 10000000 to 99999999
    for clear_line in range(1, 3):  # clear line by counting up to two when 1 display the gen number, when 2 change gen num to nothing
        if clear_line == 1:
            for i in range(1, 10+1):
                print(f"\r{num}, counting to ten: {i}", end="")
                sleep(1)
        else:
            print(f"\r", end="")

    ran_gen()

if lives == 0:
    print("You now have no lives left,\n"
          "Thanks for playing \n")
    sleep(1)
    exit("Game Exits")
