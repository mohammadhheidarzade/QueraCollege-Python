p, d= map(int , input().split())
i = 1
while not (((d * i) % p) >= 0 and ((d * i) % p) <= p // 2):
    i += 1
print(i * d)