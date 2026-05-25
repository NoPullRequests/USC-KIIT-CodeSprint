limitinput = list(map(int, input().split()))
arraysize = limitinput[0]
maxstudents = limitinput[1]

studentgroups = [int(num) for num in input().split()]

runningtotal = 0
resultindex = -1

for index in range(arraysize):
    runningtotal = runningtotal + studentgroups[index]
    
    if runningtotal > maxstudents:
        resultindex = index
        break

print(resultindex)