# Higher / Lower Guesser

import random

# get upper bound
top = int(input("Enter the range you want to guess in (larger numbers are more difficult): "))

# get "answer" number
num = random.randint(0,top)

print("Try to guess a number between and including 0 and " + str(top))


def get_guess():
    global guess
    guess = int(input("Enter a number: "))

get_guess()

while guess != num:
    if guess > num:
        print("Too high!")
    elif guess < num:
        print("Too low!")
    else:
        print("I don't know what happened")
    get_guess()
    print(guess)

print("You won!")
