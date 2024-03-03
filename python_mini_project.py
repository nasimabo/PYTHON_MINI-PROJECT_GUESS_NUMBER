import random

target = random.randint(1,100)

while True:
    user_guess = input("Enter the guess number or Quite(Q): ")
    if (user_guess == "Q"):
        break
    user_guess = int(user_guess)

    if (user_guess == target):
        print("Success : Guess the correct number !!!")
        break
    elif (user_guess < target):
        print("Your number is too small.Take a biger guess...")
    else:
        print("Your number is too big.Take a small guess...")


print("------ Game Over ------")

