word = input()
print(word)
for i in range(1 , len(word)):
    print(word[i] * (i) + word[i:])