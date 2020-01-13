#!/usr/bin/python3
"""This module takes in a string and sends a search
request to the Star Wars API
Use the string argument as the search value of the request
The body response must be JSON and converted to a Python dictionary.
Display: Number of results: <count>
Display the name of each result (see example below)
"""


import requests
import sys


if __name__ == "__main__":
    search = {'search': sys.argv[1]}
    r = requests.get("https://swapi.co/api/people/", params=search)
    json = r.json()
    print('Number of results: {}'.format(json['count']))
    for key in json['results']:
        print(key['name'])
