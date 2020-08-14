import re

cal = input()

numbers = re.split('( [+] | [=] )' , cal)
a = numbers[0]
b = numbers[2]
c = numbers[4]

def eq(withsh , real):
    withsh = withsh.split("#")
    reg = withsh[0] + '\d+' + withsh[1]
    check = re.findall(reg , real)
    if len(check) == 1 and check[0] == real:
        return real
    else:
        return -1

def printres(i , val):
    if i == 0:
        print(val)
        print(str(val) + " + " + b + " = " + c)
    elif i == 1:
        print(a + " + " + str(val) + " = " + c)
    elif i == 2:
        print(a + " + " + b + " = " + str(val))

if a.find('#') != -1:
    val = eq(a , str(int(c) - int(b)))
    if str(val) == '-1':
        print(-1)
    else:
        printres(0 , val)
elif b.find('#') != -1:
    val = eq(b , str(int(c) - int(a)))
    if str(val) == '-1':
        print(-1)
    else:
        printres(1 , val)
elif c.find('#') != -1:
    val = eq(c , str(int(a) + int(b)))
    if str(val) == '-1':
        print(-1)
    else:
        printres(2, val)
