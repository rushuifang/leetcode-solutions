class Solution {
    public String longestPalindrome(String s) {
        String res = "";
        
        for (int i = 0; i < s.length(); i++) {
            String str1 = palindrome(s, i, i);
            String str2 = palindrome(s, i, i + 1);
            String str = str1.length() > str2.length() ? str1 : str2;
            res = res.length() > str.length() ? res : str;
        }
        return res;
    }
    
    public String palindrome(String s, int l, int r) {
        while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
            l--;
            r++;
        }
        return s.substring(l + 1, r);
    }
}