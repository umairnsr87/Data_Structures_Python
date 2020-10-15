import re

x = input()

text = re.sub( r'--', "2", x )
text = re.sub( r'-.', "1", text )
text = re.sub( r'\.', "0", text )
print( text )
