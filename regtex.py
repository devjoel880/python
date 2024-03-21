import re

handle = open('regtext.txt')
numlist = list()

for line in handle:
    stuff = re.findall('[0-9]+', line)
    # make sure it finds a match so as not to print empty lists
    if stuff:
        for num_str in stuff:
            num = int(num_str)
            numlist.append(num)
print(sum(numlist))