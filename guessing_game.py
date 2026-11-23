import random

secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number: "))
    attempts += 1

    if guess > secret:
        print("Too high!")
    elif guess < secret:
        print("Too low!")
    else:
        print("Correct! You took", attempts, "attempts")
        break