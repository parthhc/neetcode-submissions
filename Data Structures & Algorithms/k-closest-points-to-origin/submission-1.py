class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            # technically dont need to sqrt as if sqrt(x) > sqrt(y), x > y
            euclidean_distance = (x ** 2) + (y ** 2)
            minHeap.append([euclidean_distance, x, y])
        
        heapq.heapify(minHeap)

        res = []
        for i in range(k):
            euclidean_distance, x, y = heapq.heappop(minHeap)
            res.append([x, y])
        
        return res