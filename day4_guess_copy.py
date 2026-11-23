import random
secretNumber = random.randint(1, 100)
print("I am thinking of a number between 1 and 100.")
attempts = 0
while True:

    print("Take a guess.")
    guess = int(input())
    attempts = attempts + 1
    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break
if guess == secretNumber:
    print("Good job! You guessed my number in " + str(attempts) + " attempts.")
    