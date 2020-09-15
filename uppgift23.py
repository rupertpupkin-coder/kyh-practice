import requests


# r = requests.get("https://proagile.se/api/publicEvents")
# t = r.json()
# pprint(t)


def run():
    r = requests.get("https://proagile.se/api/publicEvents")
    t = r.json()

    for course in t:
        if "startDate" in course:
            print(course['startDate'])


if __name__ == '__main__':
    run()
