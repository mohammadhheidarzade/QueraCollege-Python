s = input()
chs = []
for ch in s:
    if ch == '=' and len(chs) != 0:
        chs.pop()
    elif ch != '=':
        chs.append(ch)
for ch in chs:
    print(ch , end = '')