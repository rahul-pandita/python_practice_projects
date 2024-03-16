import requests
import json
import sys

# r = requests.get("https://xkcd.com/2907/")

# print(r.text)

# PRINTING OUT IMAGE    
response = requests.get("https://imgs.xkcd.com/comics/schwa.png")

# content of response in bytes
# print(response.content)

with open("image.jpeg", "wb") as comic:
    comic.write(response.content)

# status code
# print(r)

# print out attributes of r object
# print(dir(r))

# print(help(r))