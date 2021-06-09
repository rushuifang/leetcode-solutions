class Solution {
    
    private int[] nums;
    
    public Solution(int[] nums) {
        this.nums = nums;
    }
    
    public int pick(int target) {
        int count = 0;
        Random rand = new Random();
        int res = 0;
        
        for (int i = 0; i < this.nums.length; i++) {
            if (this.nums[i] == target) {
                count++;
                if (rand.nextInt(count) == 0) {
                    res = i;
                }
            }
        }
        return res;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */