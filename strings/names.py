from math import inf

def co (s):
    t = ''
    for ch in s:
        if ch not in t:
            t += ch 
    return len(t)

res = -inf

n = int(input())
for i in range(n):
    res = max(res , co(input()))
print(res)