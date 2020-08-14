k = int(input())
password = input()
def co(ch, s):
    i = s.find(ch)
    return min(i , len(s) - i)
res = 0
for i in range(k): res += co(password[i] , input())
print(res)