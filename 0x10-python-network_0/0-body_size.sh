#!/bin/bash
#Bash script that takes in URL, sends request to that URL,
curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2