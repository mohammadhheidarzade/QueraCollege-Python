fib = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
n = int(input())
for i in range(1, n + 1):
    if i in fib:
        print("+", end="")
    else:
        print("-", end="")
