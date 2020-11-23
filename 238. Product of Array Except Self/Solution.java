// # First intuition: division. I know the question asked not to... 
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] output = new int[nums.length];
        int product = 1;
        int flag = 0;
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != 0) {
                product = product * nums[i];
            } else {
                flag += 1;
            }
            
        }
        
        if (flag > 1) {
            return output;
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (flag == 1 && nums[i] == 0) {
                output[i] = product;
            } else if (flag == 1 && nums[i] != 0) {
                output[i] = 0;
            } else {
                int prod = product / nums[i];
                output[i] = prod;
            }
       
        }
        
        return output;
    }
}

// Without division
class Solution {
    public int[] productExceptSelf(int[] nums) {
        int [] output = new int[nums.length];
        output[0] = 1;
        
        int prod = 1;
        for (int i = 1; i < nums.length; i++) {
            output[i] = nums[i - 1] * prod;
            prod = prod * nums[i - 1];
        }
        
        prod = 1;
        for (int i = nums.length - 2; i >= 0; i--) {
            output[i] = nums[i + 1] * prod * output[i];
            prod = prod * nums[i + 1];
        }
        return output;
    }
}