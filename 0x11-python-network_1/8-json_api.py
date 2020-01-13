#!/usr/bin/python3
"""This module takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
The letter must be sent in the variable q
If no argument is given, set q=""
If the response body is properly JSON formatted and not empty,
display the id and name like this: [<id>] <name>
Otherwise:
    Display Not a valid JSON is the JSON is invalid
    Display No result is the JSON is empty
"""


import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        i = {'q': sys.argv[1]}
    else:
        i = {'q': ''}
    r = requests.post("http://0.0.0.0:5000/search_user", data=i)
    try:
        json = r.json()
        if len(json) == 0:
            print('No result')
        else:
            json_id = json.get('id')
            json_name = json.get('name')
            print('[{}] {}'.format(json_id, json_name))
    except:
        print("Not a valid JSON")
