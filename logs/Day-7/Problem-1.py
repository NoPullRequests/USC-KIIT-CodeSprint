wordone = input().strip()
wordtwo = input().strip()

if len(wordone) != len(wordtwo):
    print("NO")
else:
    sortedone = sorted(wordone)
    sortedtwo = sorted(wordtwo)
    
    if sortedone == sortedtwo:
        print("YES")
    else:
        print("NO")
