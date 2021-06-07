class Solution {
    public int findLeastNumOfUniqueInts(int[] arr, int k) {
        HashMap<Integer, Integer> count = new HashMap<>();
        for (int num : arr) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }
        
        int j = 0;
        int[] values = new int[count.size()];
        for (Map.Entry<Integer, Integer> entry : count.entrySet()) {
            values[j++] = entry.getValue();
        }
        
        Arrays.sort(values);
        int res = values.length;
        for (int i = 0; i < values.length; i++) {
            if (values[i] <= k) {
                res--;
                k -= values[i];
            } else { 
                break; 
            }
        }
        return res;
    }
}