#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id in the response header
"""
import sys
import requests


if __name__ == "__main__":
    uniform_r_l = sys.argv[1]

    res = requests.get(uniform_r_l)
    print(res.headers.get("X-Request-Id"))
