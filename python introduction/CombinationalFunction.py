def comb(n ,k):
    if k == 0:
        return 1
    elif n < k:
        return 0
    return comb(n-1, k-1) + comb(n-1, k)