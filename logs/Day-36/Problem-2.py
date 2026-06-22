import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    
    n = int(data[0])
    
    freq = [0] * 101
    
    for i in range(1, n + 1):
        num = int(data[i])
        freq[num] += 1
        
    unique_num = -1
  
    for i in range(1, 101):
        if freq[i] == 1:
            unique_num = i
            break
   
    position = 1
    for i in range(1, unique_num):
        position += freq[i]
        
    print(str(unique_num) + " " + str(position))

if __name__ == '__main__':
    main()
