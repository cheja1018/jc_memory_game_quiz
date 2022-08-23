# creates random integers
import random

# replies for correct, incorrect and errors
correct = "That is correct, well done!"
incorrect = "Unfortunately, that is incorrect, you lose 1 life"


# While true, show number, get users to write out number, then check if it's correct or not
valid = False
while not valid:
    # generate a random num from 0-9 x eight
    num = random.randrange(0, 9**8)
    # show number
    print(num)
    # users type in the generated numbers
    generate = int(input("Please type in the number you remember here "))

    # if the input is equal to the generated number, print correct
    if generate == num:
        print(correct)
    # if not equal to the generated number, print incorrect and show correct answer
    elif generate != num:
        print(incorrect, "the correct answer is {}".format(num))
