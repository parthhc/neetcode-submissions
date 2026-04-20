class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums: return []

        product_left_to_right = []
        product_right_to_left = []

        left_product = 1
        right_product = 1
        for i in range(len(nums)):
            if i == 0:
                product_left_to_right.append(nums[i])
                left_product = nums[i]
                product_right_to_left.insert(0, nums[len(nums) - 1 - i])
                right_product = nums[len(nums) - 1 - i]
            else:
                left_product *= nums[i]
                right_product *= nums[len(nums) - 1 - i]
                product_left_to_right.append(left_product)
                product_right_to_left.insert(0, right_product)

            
        ans = []

        for i in range(len(nums)):
            if i == 0:
                ans.append(product_right_to_left[i + 1])
            elif i == len(nums) - 1:
                ans.append(product_left_to_right[i - 1])
            else:
                ans.append(product_left_to_right[i - 1] * product_right_to_left[i + 1])
        
        return ans
            

