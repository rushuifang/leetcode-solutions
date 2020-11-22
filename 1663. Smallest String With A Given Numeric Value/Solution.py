class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        digits_modified = (k - n) // 25
        fore_digit = (k - n) % 25
        if k != 26 * n:
            return "a" * (n - digits_modified - 1) + chr(ord("a") + fore_digit) + "z" * (digits_modified)
        else:
            return "z" * n