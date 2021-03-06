class Solution {
    public char findTheDifference(String s, String t) {
        int[] count = new int[26];
        
        for (char c : s.toCharArray()) {
            count[c - 'a'] += 1; 
        }
        
        for (char c : t.toCharArray()) {
            count[c - 'a'] -= 1;
            if (count[c - 'a'] < 0) {
                return c;
            }
        }
        
        throw null;
    }
}