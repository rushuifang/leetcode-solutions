import java.util.*;
class Solution {
    public int longestPalindrome(String s) {
        Map<Character, Integer> count = new HashMap<>();
        int ans = 0;
        for (char c : s.toCharArray()) {
            count.put(c, count.getOrDefault(c, 0) + 1);
        }
        
        Collection<Integer> values = count.values();
        for (Integer i : values) {
            ans += (i / 2) * 2;
        }
        
        if (ans < s.length()) ans++;
        
        return ans;
    }
}