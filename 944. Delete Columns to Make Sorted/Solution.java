class Solution {
    public int minDeletionSize(String[] strs) {
        int m = strs.length;
        int n = strs[0].length();
        int count = 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m - 1; j++) {
                char pre = strs[j].charAt(i);
                char nxt = strs[j + 1].charAt(i);
                if (pre - nxt > 0) {
                    count++;
                    break;
                }
            }
        }
        return count;
    }
}