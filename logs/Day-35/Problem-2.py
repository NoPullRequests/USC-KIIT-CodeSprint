import sys 

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    x = int(data[1])
    weights = [int(i) for i in data[2:]]

    weights.sort()

    ans = 0
    left = 0
    right = n - 1

    while left < right:
        total = weights[left] + weights[right]

        if total == x:
            ans += 1
            low = weights[left]
            high = weights[right]

            while left < right and weights[left] == low:
                left += 1
            while left < right and weights[right] == high:
                right -= 1
        elif total < x:
            left += 1
        else:
            right -= 1

    print(ans)

if __name__ =='__main__':
    main()