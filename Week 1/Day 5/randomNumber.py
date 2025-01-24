import random

def randomNumbers():
    numRandom = random.randint(1, 10)  # Generar número aleatorio
    validate = False
    while validate == False:
        n = int(input("Enter a number between 1 and 10: "))
        if n == numRandom:
            validate = True
            return print("You win!")
        else:
            print("You lose!, try again")
randomNumbers()