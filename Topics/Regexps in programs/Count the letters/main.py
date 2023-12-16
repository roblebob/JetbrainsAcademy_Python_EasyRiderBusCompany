import re

string = input()
# Write your code here
s = str(dict(sorted({k: len(re.findall(k, string)) for k in set(string)}.items())))
s = re.sub(r'[\'\{\}]', '', s)
s = re.sub(r',\s+', '\n', s)
print(s)
