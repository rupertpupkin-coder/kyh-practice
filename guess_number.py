import random

n = random.randint(1, 100)
print("Jag tänker på ett nummer mellan 1-100. Gissa vilket?")
guesses = 1


def ask_number():
    text = input("Vad är din gissning?")
    tal = int(text)
    return tal


ask_number()


def mainloop(guesses):
    n = random.randint(1, 100)
    while True:

        text = input("Vad är din gissning?")
        tal = int(text)

        if tal == n:
            print("Snyggt! Det tog dig " + str(guesses) + " gissningar!")
            break

        if tal < n:
            print("Fel, mitt nummer är högre... Försök igen!")
            guesses = guesses + 1

        if tal > n:
            print("Fel, mitt nummer är lägre... Försök igen!")
            guesses = guesses + 1


mainloop(guesses)
