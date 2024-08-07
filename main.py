import random

def validatesIntegerRange(nro, first, last):
    try:  # Trata de hacer lo que sigue, si da error se ejecuta el except
        int(nro)
        if int(nro) >= first and int(nro) <= last:
            return False  # Validacion correcta, retorna falso para que salga del while que valida
        else:
            return True  # Validacion incorrecta, retorna verdadero para que siga en el while que valida
    except:
        return True  # Validacion incorrecta, retorna verdadero para que siga en el while que valida


guessesTaken = 0
minNumber = 1
maxNumber = 20


username = input("Hi! In order to play you need a username: \n")

number = random.randint(minNumber, maxNumber)
print(f"Well, {username}. I'm thinking of a number between {minNumber} and {maxNumber}")

while guessesTaken <5:
    guess = input("Take a guess: ")
    while (validatesIntegerRange(guess,minNumber,maxNumber)):
        guess= input(f"Invalid input. You need to enter a number between {minNumber} and {maxNumber}:\n")
    guess = int(guess)

    guessesTaken += 1

    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    elif guess == number:
        break

if guess == number:
    print(
        f"Great job {username}! You have guessed my number in {guessesTaken} guesses."
    )
elif guess != number:
    print(
        f"Unfortunately {username} the number I was thing of was {number}. Better luck next time"
    )
