result = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.index):
        result += 1
    a= sorted(word, key=word.index)
    print(a)
print(result)
