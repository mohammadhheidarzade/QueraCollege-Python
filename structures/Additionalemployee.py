n = int(input())
dp = {}
for i in range(n):
    name = input().split()[0]
    dp[name] = dp.get(name , 0) + 1
print(max(dp.values()))
