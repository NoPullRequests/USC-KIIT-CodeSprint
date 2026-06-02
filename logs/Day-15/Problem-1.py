n = int(input())

names = []
for i in range(n):
    names.append(input().strip())

def countvowels(word):
    count = 0
    vowels = "aeiou"
    for char in word:
        if char in vowels:
            count = count + 1
    return count

def sortingkey(word):
    vowelcount = countvowels(word)
    length = len(word)
    return (-vowelcount, length, word)

names.sort(key=sortingkey)

for name in names:
    print(name)