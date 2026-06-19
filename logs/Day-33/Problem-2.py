import sys 

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    k = int(data[1])

    noise = []
    for i in range(2, len(data)):
        noise.append(int(data[i]))
        
    ans = []
    for i in range(n - k + 1):
        highest = noise[i]
        for j in range(i, i + k):
            if noise[j] > highest:
                highest = noise[j]
        ans.append(highest)

    for val in ans:
        print(val, end=" ")

if __name__ == '__main__':
    main()