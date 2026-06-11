sheet = input().strip()
target = input().strip()

need = {}
for char in target:
    need[char] = need.get(char, 0) + 1

window = {}
have = 0
required = len(need)

start = 0
minlen = len(sheet) + 1
left = 0

for right in range(len(sheet)):
    char = sheet[right]
    window[char] = window.get(char, 0) + 1

    if char in need and window[char] == need[char]:
      have += 1

    while have == required:
        length = right - left + 1
        if length < minlen:
            minlen = length
            start = left
        leftchar = sheet[left]
        window[leftchar] -= 1
        if leftchar in need and window[leftchar] < need[leftchar]:
            have -= 1
        left += 1

if minlen > len(sheet):
    print(-1)
else:
    print(sheet[start : start + minlen])