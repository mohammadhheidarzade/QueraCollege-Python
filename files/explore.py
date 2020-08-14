import os
def explore(prefix , path):
    w = os.walk(path)
    res = {}
    for dir in list(w):
        for file in dir[2]:
            if file.lower().endswith("." + prefix.lower()):
                res[dir[0]] = res.get(dir[0] , 0) + 1
    return res;