#!/usr/bin/python3
"""This module is based on 9-starwars.py.
Takes in a string and sends a search request to the Star Wars API
Display: Number of results: <count>
Display the name of each result (see example below)
Must manage the pagination to display all results
For each character (people), display a list of movie (film)
names: <tabulation><film name>
"""


import requests
import sys


if __name__ == "__main__":
    search = {'search': sys.argv[1], 'page': '1'}
    r = requests.get("https://swapi.co/api/people/", params=search)
    json = r.json()
    if search['page'] == '1':
        print('Number of results: {}'.format(json['count']))
    for key in json['results']:
        print(key['name'])
        for movie in key['films']:
            r = requests.get(movie)
            j_son = r.json()
            print("\t{}".format(j_son['title']))
    while json['next'] is not None:
        r = requests.get(json['next'])
        json = r.json()
        for key in json['results']:
            print(key['name'])
            for movie in key['films']:
                r = requests.get(movie)
                j_son = r.json()
                print("\t{}".format(j_son['title']))
