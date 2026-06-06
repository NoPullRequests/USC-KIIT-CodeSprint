capacity = int(input())
queries = int(input())

cache = {}
order = []

for i in range(queries):
    line = input().split()
    op = line[0]
    
    if op == "PUT":
        key = int(line[1])
        val = int(line[2])
        
        if key in cache:
            order.remove(key)
        elif len(cache) >= capacity:
            oldest = order.pop(0)
            del cache[oldest]
            
        cache[key] = val
        order.append(key)
        
    elif op == "GET":
        key = int(line[1])
        
        if key in cache:
            print(cache[key])
            order.remove(key)
            order.append(key)
        else:
            print(-1)
