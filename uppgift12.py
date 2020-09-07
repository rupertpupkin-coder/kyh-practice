def is_it_too_long(name, max_length):

    return len(name) > max_length


def main(name):
    # students = ["anna", "beatrice", "cecilia", "doris", "esmeralda", "frida", "gunilla"]
    students = input("Ange studenternas namn med komma emellan: ").split(",")
    for name in students:
        if is_it_too_long(name, max_length):
            print(f"{name.title()} är för långt!")


if __name__ == '__main__':
    try:
        max_length = int(input("Hur långt får namnet vara?"))
    except ValueError:
        name = 5



    main(max_length)