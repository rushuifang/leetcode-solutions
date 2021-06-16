class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int len1 = nums1.length;
        int len2 = nums2.length;
        int output[] = new int[len1];
        HashMap<Integer, Integer> map = new HashMap<>();
        Stack<Integer> stack = new Stack<>();
        
        for (int i = len2 - 1; i >= 0; i--) {
            while (!stack.isEmpty() && nums2[i] > stack.peek()) {
                stack.pop();
            }
            if (!stack.isEmpty()) {map.put(nums2[i], stack.peek());}
            stack.push(nums2[i]);
        }
        

        for (int i = 0; i < len1; i++) {
            output[i] = map.getOrDefault(nums1[i], -1);
        }
        return output;
    }
}