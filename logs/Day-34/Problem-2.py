import sys

def main():
    data = sys.stdin.read().split()
    if not data: return
    
    n, x = int(data[0]), int(data[1])
    drinks = []
    idx = 2
    for _ in range(n):
        drinks.append((int(data[idx]), int(data[idx+1])))
        idx += 2
        
    dp = [0] * (x + 1)
    
    for i in range(1, x + 1):
        for cost, energy in drinks:
            if i >= cost:
                dp[i] = max(dp[i], dp[i - cost] + energy)
                
    print(dp[x])

if __name__ == '__main__':
    main()