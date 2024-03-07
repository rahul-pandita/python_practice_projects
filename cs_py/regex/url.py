import re

urls = '''
https://www.google.com
http://blahblah.com
https://youtube.com
https://www.nasa.gov'''

pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")

subbed_urls = pattern.sub(r"\2\3", urls)

print(subbed_urls)

# matches = pattern.finditer(urls)

# group 0 is everything captured
# for match in matches:
    # print(match.group(2))