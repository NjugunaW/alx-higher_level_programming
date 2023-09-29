#!/usr/bin/python3
"""Python script that takes in a URL and an email address
ends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""
import sys
import requests


if __name__ == "__main__":
    uniform_r_l = sys.argv[1]
    val = {"email": sys.argv[2]}

    res = requests.post(uniform_r_l, data=val)
    print(res.text)
