class Solution:
    def longestPalindrome(self, s: str) -> str:
        def palindrome(s, l, r):
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return s[l+1:r]
        
        max_len = ""
        for i in range(len(s)):
            sub_str1 = palindrome(s, i, i)
            sub_str2 = palindrome(s, i, i + 1)
            if len(max_len) <= len(sub_str1):
                max_len = sub_str1
            if len(max_len) <= len(sub_str2):
                max_len = sub_str2
        return max_len