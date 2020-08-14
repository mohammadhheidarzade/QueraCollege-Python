def solve(relativeAddress):
    file = open(relativeAddress)
    res = 0
    for row in file:
        row = row.strip()
        if row and row[0] != '#':
            res += 1
    file.close()
    return res