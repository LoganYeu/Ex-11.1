#Logan Yeubanks, Hannah Mercer

import re

file = input("Enter file: ")
reg = input("Enter a regular expression: ")

count = 0 

fh = open(file,'r')
for line in fh:
    line = line.rstrip()
    if re.search(reg,line):
        count += 1
    
print (count)
