import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
       
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess > random_number:
            print(f"Try again, too high!")
        elif guess < random_number:
            print(f"Try again, too low!")
    print(f"Yah, you guest number {random_number} correctly!")

guess(10)