class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = {}

        for num in nums:
            mapp[num] = mapp.get(num, 0) + 1
        
        heap = []

        for num, freq in mapp.items():
            heapq.heappush(heap, (-freq, num))

        res = []

        for _ in range(k):
            freq, num = heapq.heappop(heap)
            res.append(num)

        return res