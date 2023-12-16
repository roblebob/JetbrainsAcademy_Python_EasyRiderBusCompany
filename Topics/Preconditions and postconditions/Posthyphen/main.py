import re

print(re.search(r'(?<=-)\w+\b', input()).group())