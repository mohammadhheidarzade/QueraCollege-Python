def csv_reader(path):
    with open(path) as csv:
        for row in csv.readlines():
            yield row.rstrip().split(',')

def printcv(li):
    file = open("ans.csv" , "w")
    for row in li:
        file.write(' ,'.join(row) + '\n')

def process(path):
    res = 0
    resList = []
    for rowdata in csv_reader(path):
        res = 0
        tmpList = list(rowdata)
        for num in rowdata:
            res += 1
        tmpList.append(res)
        resList.append(tmpList)
    printcv(resList)
