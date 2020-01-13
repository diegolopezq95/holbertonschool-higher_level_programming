#!/usr/bin/python3
"""This module takes Github credentials (username and password)
and uses the Github API to display your id
"""


import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    json = r.json()
    print(json.get("id"))
