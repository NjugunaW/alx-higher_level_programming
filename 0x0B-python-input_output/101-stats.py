#!/usr/bin/python3
"""
A script that reads stdin line by line and computes metrics
"""
import sys

file_size = 0
status_tally = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
index = 0
try:
    for line in sys.stdin:
        tokens = line.split()
        if len(tokens) >= 2:
            defin = index
            if tokens[-2] in status_tally:
                status_tally[tokens[-2]] += 1
                index += 1
            try:
                file_size += int(tokens[-1])
                if defin == index:
                    index += 1
            except FileNotFoundError:
                if defin == index:
                    continue
        if index % 10 == 0:
            print("File size: {:d}".format(file_size))
            for key, value in sorted(status_tally.items()):
                if value:
                    print("{:s}: {:d}".format(key, value))
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))
