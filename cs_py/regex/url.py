import re

urls = '''
https://www.google.com
http://blahblah.com
https://youtube.com
https://www.nasa.gov'''

pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")

matches = pattern.finditer(urls)

# group 0 is everything captured
for match in matches:
    print(match.group(0))