class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_with_dist = [(x*x + y*y, x, y) for x, y in points]

        heapq.heapify(points_with_dist)

        res = []
        for i in range(k):
            _, x, y = heapq.heappop(points_with_dist)
            res.append([x, y])
        
        return res