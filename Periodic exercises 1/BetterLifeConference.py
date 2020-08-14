r ,c = map(int , input().split())
if c <= 10:
    print("Right" , 11 - r ,c )
else:
    print("Left" , 11 - r ,21 - c )