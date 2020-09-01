import random

guesses = 0
n = random.randint(1, 100)
print("Jag tänker på ett nummer mellan 1-100. Gissa vilket?")


def ask_number():
    text = input("Vad är din gissning?")
    as_number = int(text)
    return as_number


def mainloop(n,guesses):
    while True:

        as_number = ask_number()
        guesses = guesses + 1
        if as_number == n:
            print("Snyggt!")
            break

        if as_number < n:
            print("Fel, mitt nummer är högre... Försök igen!")

        if as_number > n:
            print("Fel, mitt nummer är lägre... Försök igen!")

            return guesses


guesses = mainloop(n,guesses)
print("Du gissade", guesses, "antal gånger")
