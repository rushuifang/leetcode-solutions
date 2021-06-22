class Solution {
    public int[] sumEvenAfterQueries(int[] nums, int[][] queries) {
        int sumZero = 0;
        for (int num : nums) {
            if (num % 2 == 0) {sumZero += num;}
        }
        int[] output = new int[queries.length];
        
        for (int i = 0; i < queries.length; i++) {
            int index = queries[i][1];
            int val = queries[i][0];
  
            nums[index] += val;
            if (nums[index] % 2 == 0) {
                if (val % 2 == 0) {
                    sumZero += val;
                } else {
                    sumZero += nums[index];
                }
            } else {
                if (val % 2 != 0) {
                    sumZero -= nums[index] - val;
                }
            }
            output[i] = sumZero;
        }
        
        return output;
    }
}