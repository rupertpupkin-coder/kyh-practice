import requests



def run():
    r = requests.get("https://proagile.se/api/publicEvents")
    t = r.json()
    startdatum = "Startdatum: "
    slutdatum = "Slutdatum: "
    namn = "Kursnamn: "
    for course in t:
        if 'startDate' in course:
            print(f"{namn}", course['name'])

            print(f"{startdatum}", course['startDate'])

            print(f"{slutdatum}", course['endDate'], "\n")




if __name__ == '__main__':
    run()