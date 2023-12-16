import re

print("This week you have spent: {} dollars".format(sum(list(map(int, re.findall(r'(?<=\$)\d+', input()))))))
