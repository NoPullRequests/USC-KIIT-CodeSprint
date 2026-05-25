message = input().strip()

if not message:
    print("")
else:
    result = ""
    activeletter = message[0]
    streak = 1

    for position in range(1, len(message)):
        if message[position] == activeletter:
            streak = streak + 1
        else:
            result = result + activeletter + str(streak)
            activeletter = message[position]
            streak = 1

    result = result + activeletter + str(streak)
    print(result)
