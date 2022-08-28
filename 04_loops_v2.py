import random

# replies for correct and incorrect
correct = "That is correct, well done!"
incorrect = "Unfortunately, that is incorrect, you lose 1 life"
error = "That is not a number, please try again"

lives = 3
rounds = 0


# functions go here
# random generator, correct answer
def ran_gen(cor_answer):
    # modify lives out of scope
    global lives
    global rounds
    # try/except for all possible results, incase the input isn't an integer
    try:
        # test that lives decreases each time it prints incorrect
        num = random.randrange(0, 9**8)   # number in ranges from 0-9 x 8
        print(num)  # show number
        answer = input(cor_answer)  # user input
        # comparing the user input to generated number
        if answer.lower() == "quit" or answer.lower() == "q":
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


# main routine goes here
# until lives reach 0, keep the loop going
while lives > 0:

    rounds += 1
    print("Round", rounds)
    print("You have a remainder of {} lives".format(lives))
    generate = ran_gen("What do you think the answer is ?   ")
