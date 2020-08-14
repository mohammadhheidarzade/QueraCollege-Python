i = input().split()
n = int(i[0])
ref = {ch for ch in i[1]}
for code in range(n):
    tmp = {ch for ch in input()}
    if tmp == ref:
        print("Yes")
    else:
        print("No")