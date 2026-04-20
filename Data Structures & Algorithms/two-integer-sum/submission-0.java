class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> numsAtIndex = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (numsAtIndex.containsKey(target - nums[i])) {
                int[] ans = {numsAtIndex.get(target - nums[i]), i};
                return ans;
            }
            numsAtIndex.put(nums[i], i);
        }
        int[] ans = {};
        return ans;
    }
}
