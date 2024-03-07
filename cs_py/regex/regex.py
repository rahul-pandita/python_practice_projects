import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] backslash | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = "Start a sentence and then bring it to an end"

# pattern to search for 
pattern = re.compile(r"[89]00[-.]\d{3}[-.]\d{4}")

# matches = pattern.finditer(text_to_search)

# for match in matches:
    # print(match)

with open("user_data.txt", "r") as f:
    contents = f.read()
    matches = pattern.finditer(contents)

    for match in matches:
        print(match)

