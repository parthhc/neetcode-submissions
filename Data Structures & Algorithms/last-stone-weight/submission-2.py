class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [-i for i in stones]
        heapq.heapify(arr)

        while len(arr) > 1:
            x = heapq.heappop(arr)
            y = heapq.heappop(arr)
            if y > x:
                heapq.heappush(arr, x - y)
        
        arr.append(0)
        return abs(arr[0])