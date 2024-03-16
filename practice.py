import requests
import json
import sys

if len(sys.argv) != 2:
    sys.exit()

r = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(json.dumps(r.json(), indent=2))