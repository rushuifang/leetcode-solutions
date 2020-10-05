class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += (ord(s[::-1][i]) - 64) * 26 ** i
        return res