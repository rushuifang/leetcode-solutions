class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPali(i, j):
            return all(s[k] == s[j - k + i] for k in range(i, j))

        for i in range(len(s) // 2):
            j = len(s) - i - 1
            if s[i] != s[j]:
                return isPali(i + 1, j) or isPali(i, j - 1)
        return True
