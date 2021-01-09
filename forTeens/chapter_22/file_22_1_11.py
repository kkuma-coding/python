import random

secret_number = random.randrange(1, 101)

attempts = 1

guess = int(input("Enter a guess: "))
while guess != secret_number:
    if guess > secret_number:
        print("Your guess is bigger than my secret number. Try again.")
    else:
        print("Your guess is smaller than my secret number. Try again.")

    attempts += 1

    guess = int(input("Enter a guess: "))
    
print("You found it!")
print("Attempts:", attempts)
