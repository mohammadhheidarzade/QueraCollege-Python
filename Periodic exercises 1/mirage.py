t = int(input())
for i in range(t):
    x,y = map(int , input().split())
    if not (x == y or x - 2 == y):
        print(-1)
    else:
        if x % 2 == 0:
            print(x + y)
        else:
            print(x + y - 1)