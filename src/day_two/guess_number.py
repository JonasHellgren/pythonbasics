import random
from operator import truediv

secret=random.randint   (1,20)
guesses=set()

while True:
    guess=int(input("Give guess (1-20):"))

    if (guess in guesses):
        print("Already guessed")
        continue

    guesses.add(guess)

    if (guess==secret):
        print("Correct")
        break;
    elif (guess<secret):
        print("To low")
    else:
        print("To high")






