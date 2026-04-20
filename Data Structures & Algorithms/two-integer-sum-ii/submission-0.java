class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1; 

        while (left < right) {
            int[] ans = {left+1, right+1};
            if (numbers[left] + numbers[right] == target) {
                return ans;
            }
            if (numbers[left] + numbers[right] > target) {
                right--;
            } else if (numbers[left] + numbers[right] < target) {
                left++;
            }
        }
        int[] ans = {};
        return ans;
    }
}
