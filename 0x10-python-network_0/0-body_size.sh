#!/bin/bash
# Displays the body size of a request
curl -s "$1" | wc -c
