n ,m = map(int , input().split())
k = int(input())
field = [[0 for i in range(m + 1)] for i in range(n + 1)]


def valid(i , j):
    if i < 1 or i > n:
        return False
    elif j < 1 or j > m:
        return False
    return True


def cal(i ,j):
    res = 0
    for it in range(-1 , 2):
        for jt in range(-1 , 2):
            itt = i + it
            jtt = j + jt
            if valid(itt ,jtt) and field[itt][jtt] == 1:
                res += 1
    print(res , end = ' ')



for i in range(k):
    nt ,mt = map(int , input().split())
    field[nt][mt] = 1
for i in range(1 , n+1):
    for j in range(1 , m+1):
        if (field[i][j] == 1):
            print('* ' ,end = '')
        else:
            cal(i ,j)
    print()
