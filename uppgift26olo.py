import requests
import json
from pprint import pprint

def main():

    user_input = input("Vilken film vill du veta mer om?")
    movie = requests.get("http://www.omdbapi.com/", params={"t": f"{user_input}", "apikey": "9f6d550c"})

    text = movie.text
    result = json.loads(text)
    pprint(result)


    print(f"Skådisar: {result['Actors']}")
    print(f"IMDB betyg: {result['imdbRating']}")
    print


main()