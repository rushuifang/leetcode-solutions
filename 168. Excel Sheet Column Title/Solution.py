class Solution:
    def convertToTitle(self, n: int) -> str:
        s = ""
        while n > 0:
            n -= 1
            i = n % 26
            n = n // 26
            s += chr(i + 65)
        return s[::-1]