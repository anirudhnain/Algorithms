import heapq
for _ in range(int(input())):
    t = [int(x) for x in input().split()[1:]]
    n = t[0]
    if n == 0:
        print (0)
        continue
    a = sorted(t)
    heap = {x:[] for x in a}
    for x in a:
        print (x)
        if x-1 in heap and len(heap[x-1]) > 0:
            heapq.heappush(heap[x], heapq.heappop(heap[x-1])+1)
        else:
            heapq.heappush(heap[x], 1)
        print (heap[x] )
    print (min(heap[x][0] for x in heap if len(heap[x])!=0))