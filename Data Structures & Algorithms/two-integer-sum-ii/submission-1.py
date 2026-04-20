class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            leftNum = numbers[l]
            rightNum = numbers[r]
            if leftNum + rightNum > target:
                r -= 1
            elif leftNum + rightNum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return [r + 1, l + 1]