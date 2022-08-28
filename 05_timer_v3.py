from time import sleep

# when range is 1, print a line, when it's not 1 print another line
for delete_line in range(1, 3):
    if delete_line == 1:
        print(f"\rhello world", end="")

    else:
        print(f"\rdelete previous line", end="")
    sleep(6)
