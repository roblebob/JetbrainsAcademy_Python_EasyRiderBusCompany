import re

pattern = re.compile(r'(0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/[1-2]\d{3}')
print(bool(pattern.match(input())))
