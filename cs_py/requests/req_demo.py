import requests

r = requests.get("https://xkcd.com/2903/")

print(r.text)

# see all of the attributes and methods available for an object
# print(dir(r))

# detailed explanation of above
# print(help(r))