import random

a = random.randrange(1,50)
guess = int(input("Enter any number: "))
while a != guess:
    if guess < a:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > a:
        print("Too High!")
        guess = int(input("Enter number again: "))
    else:
        break
print("You guessed it right!")
