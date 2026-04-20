class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = [-i for i in nums]

        heapq.heapify(arr)

        res = -1
        for i in range(k):
            res = heapq.heappop(arr)

        return res * -1