import re


sentence = 'Do I like cats? Yes!!'
template = r'Do I like cats\? Yes!!'
tem = re.match(template, sentence)