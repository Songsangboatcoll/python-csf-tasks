import random

secret_number = random.randint(1,100)
while True:
    guess = int(int("Guess a number between 1 to 100 inclusive: "))
    if guess> secret_number:
        print("Too high")
    elif guess < secret_number:
        print("Too loe")
    else:
        print("Congratulation! Your guess is correct")