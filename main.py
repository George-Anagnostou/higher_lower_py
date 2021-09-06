# Higher / Lower Guesser

import random

# get upper bound
top = int(input("Enter the range you want to guess in (larger numbers are more difficult): "))

# get "answer" number
num = random.randint(0,top)

## debugging
print(num)

print("Try to guess a number between and including 0 and " + str(top))

def ask_guess():
    guess = int(input("Enter your number: "))
    return guess

ask_guess()
print(guess)

while guess != num:
    if guess > num:
        print("Too high!")
    elif guess < num:
        print("Too low!")
    else:
        print("I don't know what happened")
    print(guess)
    ask_guess()

print("You won!")
