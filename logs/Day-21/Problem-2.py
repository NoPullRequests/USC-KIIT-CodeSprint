n = int(input())

past = {}

def fib(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    if x in past:
        return past[x]
    
    past[x] = fib(x - 1) + fib(x - 2)
    return past[x]

print(fib(n))
