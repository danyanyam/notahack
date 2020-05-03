import re


with open('./devices.txt') as f:
    text = f.read()

pattern = re.compile('(<)(.+)(>)')
found = re.search(pattern, text).group(2)
print(found)
