def wordcount():

    text = input("Skriv en text: ").split()
    print(f"Du skrev {len(text)} ord")


if __name__ == '__main__':

    wordcount()
