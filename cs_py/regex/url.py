import re

urls = '''
https://www.google.com
http://blahblah.com
https://youtube.com
https://www.nasa.gov'''

pattern = re.compile(r"https?://(www\.)?\w+\.\w+")

matches = pattern.finditer(urls)

for match in matches:
    print(match)