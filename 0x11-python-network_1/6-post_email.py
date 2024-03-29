#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response.
Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":url = sys.argv[1]
  r = requests.post(url, data={'email':sys.argv[2]})
  print('Your email is : {}'.format(r.content['email']))
