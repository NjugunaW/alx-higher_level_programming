#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    uniform_r_l = sys.argv[1]

    res = requests.get(uniform_r_l)
    if res.status_code >= 400:
        print("Error code: {}".format(esr.status_code))
    else:
        print(res.text)
