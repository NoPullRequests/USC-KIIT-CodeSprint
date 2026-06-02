total = int(input())

students = []
while len(students) < total:
    line = input().strip()
    if line:
        students = list(map(int, line.split()))

low = 0
mid = 0
high = total - 1

while mid <= high:
    if students[mid] == 0:
        temp = students[low]
        students[low] = students[mid]
        students[mid] = temp
        
        low = low + 1
        mid = mid + 1
    elif students[mid] == 1:
        mid = mid + 1
    else:
        temp = students[high]
        students[high] = students[mid]
        students[mid] = temp
        
        high = high - 1

for i in range(total):
    if i == total - 1:
        print(students[i])
    else:
        print(students[i], end=" ")

