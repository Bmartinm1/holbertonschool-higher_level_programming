#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digitCheck = number[-1]
if (digitCheck > 5):
    print("Last digit of {:d} is {:d} and is greater than 5",
          number, digitCheck)
elif (digitCheck == 0):
    print("Last digit of {:d} is {:d} and is 0", number, digitCheck)
else:
    print(
        "Last digit of {:d} is {:d} and is less than 6 and not 0", number, digitCheck)
