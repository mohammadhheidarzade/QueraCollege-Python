import re


try:
    while True:
        line = input()
        if re.match("^\s*[+-]?(\d+(.\d+)?)([eE][+-]?\d+)?\s*$" , line):
            print("LEGAL")
        else:
            print("ILLEGAL")
except:
    pass