// TLE

class Solution {
    int counts = 0;
    public int minIncrementForUnique(int[] nums) {
        Set<Integer> set = new HashSet<>();
        Map<Integer, Integer> freq = new HashMap<>();
        
        
        for (int x : nums) {set.add(x);}
        for (int x : nums) {freq.put(x, freq.getOrDefault(x, 0) + 1);}
        
        freq.forEach((k, v) -> {
            while (v > 1) {
                int x = k;
                while (set.contains(x)) {
                    x++;
                    counts++;
                }
                set.add(x);
                v--;
            }
        });
        
        return counts;
    }
}


// Use counts
class Solution {
    
    public int minIncrementForUnique(int[] nums) {
        int[] counts = new int[100000];
        for (int num : nums) {counts[num]++;}
        int taken = 0;
        int ans = 0;
        
        for (int i = 0; i < 100000; i++) {
            if (counts[i] > 1) {
                taken += counts[i] - 1;
                ans -= i * (counts[i] - 1);
            } else if (taken > 0 && counts[i] == 0) {
                taken--;
                ans += i;
            }
        }
        return ans;
        
    }
}