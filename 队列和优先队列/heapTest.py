import heapq
import random


a=[]
for i in range(10):

    j=random.randint(1,100)
    a.append(j)
# print(a)
# print(heapq.heappop(a))
# heapq.heapify(a)
# print(a)
# print(heapq.heappop(a))
# b=[]
# heapq.heappush(b,1)
# heapq.heappush(b,2)
# heapq.heappush(b,1)
# heapq.heappush(b,1)
# print(b)
a=[9,2,45,6,23,1,42]
b=[]
for i in a:
    heapq.heappush(b,i)

print(b)