#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8).
You have to manage urllib.error.HTTPError exceptions and
print: Error code: followed by the HTTP status code.
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('ascii')
            print(html)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
    except URLError as e:
        print(e.reason)
  
