# creates random integers
import random

# replies for correct and incorrect and errors
correct = "That is correct, well done!"
incorrect = "Unfortunately, that is incorrect, you lose 1 life"
error = "That is not a number, please try again"


# functions go here...
# random generator, correct answer
def ran_gen(cor_answer):
    try:
        # number in ranges from 0-9 x 8
        num = random.randrange(0, 9**8)
        # show number
        print(num)
        # user input
        answer = int(input(cor_answer))
        # comparing the user input to generated number
        # if correct print correct
        # if wrong print incorrect
        if answer == num:
            print()
            print(correct)
            return answer
        else:
            print()
            print(incorrect, "the correct answer is {}".format(num))
            return answer

    except ValueError:
        print(error)


# main routine goes here
# print the question
generate = ran_gen("What do you think the answer is ?   ")
