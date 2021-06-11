class Solution {
    public int numberOfSubstrings(String s) {
        int i = 0, j = 0, len = s.length();
        int[] count = new int[3];
        char[] arr = s.toCharArray();
        int res = 0;
        
        while (j < len) {
            count[arr[j] - 'a']++;
            while (i < j && count[0] > 0 && count[1] > 0 && count[2] > 0) {
                res += len - j;
                count[arr[i++] - 'a']--;
            }
            j++;
        }
        
        return res;
    }
}