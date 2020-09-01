import random

n = random.randint(1, 100)
print("Jag tänker på ett nummer mellan 1-100. Gissa vilket?")
guesses = 1


def ask_number():
    text = input("Vad är din gissning?")
    tal = int(text)
    return tal


def mainloop(guesses):
    n = random.randint(1, 100)
    while True:

        as_number = ask_number()

        if as_number == n:
            print("Snyggt! Det tog dig " + str(guesses) + " gissningar!")
            break

        if as_number < n:
            print("Fel, mitt nummer är högre... Försök igen!")
            guesses = guesses + 1

        if as_number > n:
            print("Fel, mitt nummer är lägre... Försök igen!")
            guesses = guesses + 1


mainloop(guesses)
