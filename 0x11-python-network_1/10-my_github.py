#!/usr/bin/python3
"""Python script that takes your GitHub credentials 
and uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth_entication import HTTPBasicauth_entication


if __name__ == "__main__":
    auth_entication = HTTPBasicauth_entication(sys.argv[1], sys.argv[2])
    res = requests.get("https://api.github.com/user", auth_entication=auth_entication)
    print(res.json().get("id"))
