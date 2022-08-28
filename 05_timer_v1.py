# import time for the seconds needed to wait for
from time import sleep

# Print hello world
print("Hello World")
# print 1 - 10 one second apart, ending the previous number before the next
for i in range(1, 10+1):
    print(f"\r{i}", end="")
    sleep(1)


# skip 50 lines so that the code cannot be seen
for i in range(1, 50):
    print("")  # blank lines
testing = input("Just a testing")
