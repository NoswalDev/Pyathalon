#I'm really fed up with the print line and argv stuff right now.

from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def printLine(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print_all(current_file)

rewind(current_file)

current_line = 1
printLine(current_line,current_file)
