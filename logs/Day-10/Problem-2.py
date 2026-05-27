total = int(input())

nums = []
while len(nums) < total:
    line = input().strip()
    if line:
        nums = list(map(int, line.split()))

target = int(input())

for i in range(total):
    for j in range(0, total - i - 1):
        if nums[j] > nums[j + 1]:
            temp = nums[j]
            nums[j] = nums[j + 1]
            nums[j + 1] = temp

found = False

for i in range(total - 2):
    fixed = nums[i]

    left = i + 1
    right = total - 1

    while left < right:
        currentsum = fixed + nums[left] + nums[right]

        if currentsum == target:
            found = True
            break
        elif currentsum < target:
            left = left + 1
        else:
            right = right - 1
            
    if found == True:
        break

if found == True:
    print("YES")
else:
    print("NO")
