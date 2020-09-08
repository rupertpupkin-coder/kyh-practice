FRUITS = ['banana', 'apple', 'orange']
CARS = ['volvo', 'ford', 'tesla']
COLOR = ["red", "blue", "green", "yellow", "black"]


def run():
    basket = ['volvo', 'is', 'red', 'an', 'orange', 'apple', 'black']
    cars = []

    fruits = []

    color = []
    rest = []

    for item in basket:
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
