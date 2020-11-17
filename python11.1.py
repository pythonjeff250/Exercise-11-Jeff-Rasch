import re
fname = input("Enter a file name:")
regex = input("Enter a regular expression:")
fhandle = open(fname)
counter = 0
for line in fhandle:
    if line.startswith('From '):
        line = line.rstrip()
    if re.search(regex, line):
        counter += 1

print(fname+ ' had '+ str(counter)+' lines that matched '+ regex)
