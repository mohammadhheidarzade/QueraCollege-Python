from datetime import datetime
date = datetime.strptime(input(), '%Y-%m-%d')

date2 = datetime.strptime("1999-01-14",'%Y-%m-%d')

days = (date - date2).days

if days < 0:
    print('Not yet born')
else:
    print(days)