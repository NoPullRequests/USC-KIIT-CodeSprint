text = input()
n = len(text)

compressed = ""
i = 0

while i < n:
    count = 1
    while i + 1 < n and text[i] == text[i + 1]:
        count = count + 1
        i = i + 1
        
    compressed = compressed + text[i] + str(count)
    i = i + 1

print(compressed)
