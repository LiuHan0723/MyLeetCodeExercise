import heapq

def topK(nums,k):

    pq = []
    d = {}
    for i in nums:
        d.setdefault(i, 0)
        d[i] += 1
    items = list(d.items())

    for j in range(len(items)):
        if len(pq)==k:

            if pq[0][0]<items[j][1]:
                heapq.heappop(pq)
                heapq.heappush(pq, (items[j][1],items[j][0]))

        else:
            heapq.heappush(pq,(items[j][1],items[j][0]))



    return [i[0] for i in pq]

if __name__ == '__main__':
    topK([3,0,1,0],1)