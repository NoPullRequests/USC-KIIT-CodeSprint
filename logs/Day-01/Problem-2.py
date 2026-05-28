n = 6
marks = [78, 85, 91, 78, 88, 95]
flag = 0

for i in range(n):
    for j in range(i+1, n):
        if marks[i]==marks[j]:
            flag = 1
            break

if flag==1:
    print("YES")
else:
    print("NO")
