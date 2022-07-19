#!/usr/bin/env python3
import requests
from os import listdir

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"


def upload(file, url):
    with open(file, "rb") as opened:
        requests.post(url, files={"file": opened})


# gather list of image files:
files = [
    "supplier-data/images/" + f
    for f in listdir("supplier-data/images/")
    if f.endswith(".jpeg")
]
for file in files:
    upload(file, url)

    