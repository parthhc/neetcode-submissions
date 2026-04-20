class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = {}

        for n in nums:
            mapp[n] = 1 + mapp.get(n, 0)
        
        heapp = []

        for key, value in mapp.items():
            heapq.heappush(heapp, (-value, key))

        res = []

        for i in range(k):
            res.append(heapq.heappop(heapp)[1])

        return res