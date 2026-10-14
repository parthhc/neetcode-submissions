class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        bucket_sort = [[] for i in range(len(nums) + 1)]

        for num, occ in freq.items():
            bucket_sort[occ].append(num)

        res = []
        for i in range(len(bucket_sort) - 1, -1, -1):
            res.extend(bucket_sort[i])
            while len(res) > k:
                res.pop()

            if len(res) == k:
                break

        return res