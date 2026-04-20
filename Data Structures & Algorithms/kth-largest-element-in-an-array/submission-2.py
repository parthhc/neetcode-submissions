import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # gonna try quickselect, if not just do the heap solution

        k = len(nums) - k

        def quickselect(arr, target):
            pivot = random.choice(arr)

            less_than = []
            eq_to = []
            greater_than = []

            for i in range(len(arr)):
                if arr[i] == pivot:
                    eq_to.append(arr[i])
                elif arr[i] < pivot:
                    less_than.append(arr[i])
                else:
                    greater_than.append(arr[i])

            if target < len(less_than):
                return quickselect(less_than, target)
            elif target >= len(less_than) + len(eq_to):
                return quickselect(greater_than, target - len(less_than) - len(eq_to))
            else:
                return pivot

        return quickselect(nums, k)