def check_registration_rules(**kwargs):
    res = []
    for u, p in kwargs.items():
        if len(u)  < 4 or \
            u == 'quera' or \
                u == 'codecup': continue
        if len(p) < 6: continue
        try:
            f = int(p)
        except:
            res.append(u)
    return res