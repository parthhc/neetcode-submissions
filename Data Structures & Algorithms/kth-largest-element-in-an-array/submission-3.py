class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        copy = [-n for n in nums]
        heapq.heapify(copy)

        res = -1
        while k > 0:
            res = heapq.heappop(copy) * -1
            k -= 1
        
        return res