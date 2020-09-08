# uppgift14.py
'''
13.1 Utan att köra programmet längst ned i denna uppgift, beskriv vad det gör för varandra! - Done
13.2 Modifiera programmet så att inte bara "kind" skrivs ut i write_things-funktionen, utan också antalet things t.ex "CARS (3 st)"
13.3 Lägg till en ny kategori av saker till programmet, hitta på något! Och lägg i items av denna sort i en ny lista, som skrivs ut på slutet.
13.4 Skriv ut items i alfabetisk ordning.
13.5 Låt användaren mata in innehåll i basket i form av en kommaseparerad sträng, t.ex. kan användaren mata in "banana,apple, orange" och det tolkas som listan ["banana", "apple", "orange"]
'''

FRUITS = ['banana', 'apple', 'orange']
CARS = ['volvo', 'ford', 'tesla']
COLOR = ["red", "blue", "green", "yellow", "black"]


def run():
    basket = input("Skriv lista: ").split(",")  # gör om inputen till en lista som bryter på ,

    cars = []
    fruits = []
    color = []
    rest = []

    for item in basket:
        item = item.strip()  # Tar bort onödiga mellanslag
        if item in CARS:
            cars.append(item)

        elif item in FRUITS:
            fruits.append(item)

        elif item in COLOR:
            color.append(item)

        else:
            rest.append(item)

    write_things(sorted(cars), 'Cars')  # Skickar in en sorterad lista sorted(cars) + namnet.
    write_things(sorted(fruits), 'Fruits')
    write_things(sorted(color), "Colors")
    write_things(sorted(rest), 'Misc')


def write_things(items, kind):
    print(f"{kind.upper()}  ({len(items)}st)")
    for item in items:
        print(f" {item}")


if __name__ == '__main__':

    run()
