from math import pi


def get_func(ls):
    res = []

    for l in ls:
        if l == 'square':
            res.append(lambda x: x*x)
        elif l == 'circle':
            res.append(lambda x: x*x*pi)
        elif l == 'rectangle':
            res.append(lambda x, y: x * y)
        elif l == 'triangle':
            res.append(lambda x, y: x * y / 2)
    return res