class Solution {
    public int[] findErrorNums(int[] nums) {
        int[] res = new int[2];
        int dup = 0;
        int missing = 0;
        
        for (int i = 0; i < nums.length; i++) {
            int index = Math.abs(nums[i]) - 1;
            if (nums[index] > 0) {
                nums[index] *= -1;
            } else {
                dup = index + 1;
            }
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                missing = i + 1;
            }
        }
        
        res[0] = dup;
        res[1] = missing;
        return res;
    }
}