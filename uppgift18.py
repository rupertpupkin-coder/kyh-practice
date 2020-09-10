
people = {
    "Fredrik": "0702778511",
    "Olof": "123456789",
    "Lisa": "9999999999",
    "Bodil": "555-666-789",
}


vem = input(f"Du har {len(people)} kontakter. Vem vill du ringa?")

if vem not in people:
    print("Sorry hörru, vet ej vem detta är. Har endast VIP i min katalog")
else:
    number = people[vem]
    print(f"Numret till {vem} är {number}")
