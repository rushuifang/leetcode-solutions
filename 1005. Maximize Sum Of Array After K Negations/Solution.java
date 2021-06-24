class Solution {
    public int largestSumAfterKNegations(int[] nums, int k) {
        Arrays.sort(nums);
        int sum = 0;
        int idx = 0;
        
        if (nums[0] > 0 && k % 2 != 0) {
            nums[0] = - nums[0];
        } else if (nums[0] < 0) {
                while (k > 0 && nums[idx] < 0 && idx < nums.length) {
                    nums[idx] = -nums[idx++];
                    k--;
                }
                if (k % 2 != 0) {
                    int index = nums[idx] > nums[idx - 1] ? idx - 1 : idx;
                    nums[index] = -nums[index];
                }
            }
        
        for (int x : nums) {
            sum += x;
        }
        
        return sum;
    }
}