class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapp = {} # key: num, value: frequency
        for i in range(len(nums)):
            if nums[i] in mapp:
                mapp[nums[i]] += 1
            else:
                mapp[nums[i]] = 1
        
        heap = []

        for key, value in mapp.items():
            heapq.heappush(heap, (-value, key))

        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])

        
        return ans