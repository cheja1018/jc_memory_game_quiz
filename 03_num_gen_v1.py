# creates random integers
import random

# using a while loop, test
for items in range(0, 20):
    # number in ranges from 0-9 x 8
    num = random.randrange(0, 9**8)
    # show number
    print(num)
