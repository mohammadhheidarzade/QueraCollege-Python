n = int(input())
users = {}
m = 0
name = input().split()[2]
for i in range(n):
    age = input().split()[1]
    city = input().split()[1]
    users[(name , age , city)] = []
    next_line = input()
    while((next_line := input())[0] != '-'):
        if next_line.split()[0] != '-':
            m = int(next_line.split()[0])
            break
        album = next_line.split()[1]
        users[(name,age,city)].append(album);
    else:
        name = next_line.split()[2]
albums = []
for i in range(m):
    name = input().split()[2]
    singer = input().split()[1]
    genre = input().split()[1]
    tracks = input().split()[1]
    albums.append((name , singer , genre , tracks))
q = int(input())
def findUser(username):
    for user in users:
        if user[0] == username:
            return user
    return None
def findAlbum(albumName):
    for album in albums:
        if album[0] == albumName:
            return album
def first(username, singer):
    res = 0
    user = findUser(username)
    if user == None:
        print(res)
        return
    for albumName in users[user]:
        album = findAlbum(albumName)
        if album[1] == singer:
            res += int(album[3])
    print(res)
def second(username, genre):
    res = 0
    user = findUser(username)
    if user == None:
        print(res)
        return
    for albumName in users[user]:
        album = findAlbum(albumName)
        if album[2] == genre:
            res += int(album[3])
    print(res)
def third(age, singer):
    res = 0

    for user in users:
        if user[1] == age:
            for albumName in users[user]:
                album = findAlbum(albumName)
                if album[1] == singer:
                    res += int(album[3])
    print(res)
def fourth(age, genre):
    res = 0
    for user in users:
        if user[1] == age:
            for albumName in users[user]:
                album = findAlbum(albumName)
                if album[2] == genre:
                    res += int(album[3])
    print(res)
def fifth(city, singer):
    res = 0
    for user in users:
        if user[2] == city:
            for albumName in users[user]:
                album = findAlbum(albumName)
                if album[1] == singer:
                    res += int(album[3])
    print(res)
def sixth(city, genre):
    res = 0
    for user in users:
        if user[2] == city:
            for albumName in users[user]:
                album = findAlbum(albumName)
                if album[2] == genre:
                    res += int(album[3])
    print(res)
def setCommand(i):
    if i == 1  :return first
    elif i == 2:return second
    elif i == 3:return third
    elif i == 4:return fourth
    elif i == 5:return fifth
    elif i == 6:return sixth
for i in range(q):
    next_line = input().split()
    command = int(next_line[0])
    setCommand(command)(next_line[1] , next_line[2])