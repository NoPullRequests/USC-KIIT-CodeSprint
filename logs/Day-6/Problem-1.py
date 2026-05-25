password = input().strip()

hasbigletter = False
hassmallletter = False
hasnumber = False

for character in password:
    if character.isupper():
        hasbigletter = True
    elif character.islower():
        hassmallletter = True
    elif character.isdigit():
        hasnumber = True

if hasbigletter and hassmallletter and hasnumber:
    print("STRONG")
else:
    print("WEAK")
