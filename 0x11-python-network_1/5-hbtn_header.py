#!/usr/bin/python3
# A script that get the X-Request-Id using python requests module
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))
