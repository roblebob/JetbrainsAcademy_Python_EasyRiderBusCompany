import re

string = input()
# your code here
pattern = re.compile(r'(?<=\w)(ou)(?=\w+)')
print(pattern.sub('o', string))