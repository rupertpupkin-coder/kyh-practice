import requests
import datetime
import json


def run():
    r = requests.get("https://proagile.se/api/publicEvents")
    course_list = r.json()
    startdatum = "Startdatum: "
    slutdatum = "Slutdatum: "
    namn = "Kursnamn: "
    today = datetime.datetime.today()

    # year = input("Ange år: ")
    # month = input("Ange månad: ")
    #
    # for courses in daterange:
    #     if

    for course in course_list:
        if 'startDate'  in course:
            print(f"{namn:>12}{course['name']:<100}")

            print(f"{startdatum:>12}{course['startDate']:<100}")

            print(f"{slutdatum:>12}{course['endDate']:<100} \n")




if __name__ == '__main__':
    run()
# startdate = "2020-10-01"
# enddate =   "2020-10-31"
# coursedate = course['startDate']
# if startdate < coursedate and coursedate < enddate:
#     print(f"{namn:>12}{course['name']:100}")
#     print(f"{startdatum:>12}{course['startDate']:100}")
#     print(f"{slutdatum:>12}{course['endDate']:100} \n")