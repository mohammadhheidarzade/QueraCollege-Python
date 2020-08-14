b = False
for i in range(1 , 6):
    s = input()
    if "MOLANA" in s or "HAFEZ" in s:
        b = True
        print(i , end = ' ')
if not b:
    print("NOT FOUND!")