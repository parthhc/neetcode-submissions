class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> seenNums = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            if (seenNums.contains(nums[i])) {
                return true;
            }
            seenNums.add(nums[i]);
        } 
        return false;
    }
}
