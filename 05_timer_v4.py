import random
from time import sleep

# replies for correct and incorrect
correct = "That is correct, well done!"
incorrect = "Unfortunately, that is incorrect, you lose 1 life"
error = "That is not a number, please try again"

lives = 3
rounds = 0


# functions go here
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


# main routine goes here
# until lives reach 0, keep the loop going
while lives > 0:

    rounds += 1
    print("Round", rounds)
    print("You have a remainder of {} lives".format(lives))  # lives decrease each time it prints incorrect
    num = random.randrange(0, 9**8)   # number in ranges from 0-9 x 8

    for clear_line in range(1, 3):
        if clear_line == 1:
            for i in range(1, 10+1):
                print(f"\r{num}, counting to ten {i}", end="")
                sleep(1)
        else:
            print(f"\r", end="")

    ran_gen()

    if lives == 0:
        print("You now have no lives left,\n"
              "Thanks for playing \n")
        exit("Game Exits")
    else:
        enter_continue()
