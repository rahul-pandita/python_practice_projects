import requests

# r = requests.get("https://xkcd.com/2903/")
r = requests.get("https://imgs.xkcd.com/comics/earth_venus_venn_diagram.png")

with open("comic.png", "wb") as f:
    f.write(r.content)

# see all of the attributes and methods available for an object
# print(dir(r))

# detailed explanation of above
# print(help(r))