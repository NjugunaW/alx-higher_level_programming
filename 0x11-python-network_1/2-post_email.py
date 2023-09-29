#!/usr/bin/python3
""" Python script that takes in a URL and an email, sends a POST request to the passed URL
"""


import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    unifrom_r_l = sys.argv[1]
    val = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(val).encode("ascii")

    request = urllib.request.Request(unofprm_r_l, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))

