import random


def main():

    en_app = ["En tidning", "En gåta", "Ett TV-spel", "Olika hieroglyfer"]
    mobiltelefonen = ["tegelsten", "avancerad dator", "walkie-talkie", "diverse skräppost"]
    nedladdning = ["läsas upp av en", "krypteras av en", "omvandlas till en"]
    ursprung = ["utomjordingar", "hypokondriker", "bestigare av Kebnekaise"]
    virus = ["har tagit på sig för stora skor", "har ätit en banan med skal på", "har hoppat fallskärm från ett plan men glömde fallskärmen"]
    jag = ["Flera", "Alla jag känner", "Min släkt", "Jag pratade lite med Donald Trump och han"]


    print(f"""{en_app[random.randint(0, 3)]} som kan {nedladdning[random.randint(0,2)]} {mobiltelefonen[random.randint(0,3)]} ska varna {ursprung[random.randint(0, 2)]} som kommit nära någon som {virus[random.randint(0,2)]}.
– {jag[random.randint(0,3)]} tycker att ni i Sverige borde överväga att göra något liknande, säger Markku Tervahauta, generaldirektör för
Finska institutet för hälsa och välfärd, THL.""")


if __name__ == '__main__':
    main()
