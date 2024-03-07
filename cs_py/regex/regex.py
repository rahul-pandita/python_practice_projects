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

emails = '''
BabbluPJohnson@gmail.com
tommy.chaudhary@manipal.edu
rahul-123-pandita@my-work.net
'''

# pattern to search for 
pattern = re.compile(r"start", re.IGNORECASE)

matches = pattern.search(sentence)

print(matches)


