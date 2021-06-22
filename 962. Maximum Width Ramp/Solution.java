class Solution {
    public int maxWidthRamp(int[] nums) {
        int N = nums.length;
        int max = 0;
        
        for (int i = 0; i < N; i++) {
            for (int j = N - 1; j > i; j--) {
                if (nums[j] >= nums[i]) {
                    max = Math.max(max, j - i);
                    break;
                }
                
            }
        }
        return max;
    }
}