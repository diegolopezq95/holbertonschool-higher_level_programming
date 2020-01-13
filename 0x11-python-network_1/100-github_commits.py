#!/usr/bin/python3
"""This module list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
You must use the Github API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""


import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits"\
        .format(sys.argv[2], sys.argv[1])
    r = requests.get(url)
    json = r.json()
    i = 0
    for key in json:
        if i < 10:
            print("{}: {}".format(key['sha'],\
                                  key['commit']['author']['name']))
            i += 1
