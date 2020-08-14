import statistics 
def calc(li):
    average = sum(li) / len(li)
    middle = statistics.median(li)
    mx = max(li)
    return average,middle,mx