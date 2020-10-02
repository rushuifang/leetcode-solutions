class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(el) for el in digits]
        s = "".join(digits)
        return [int(el) for el in str(int(s) + 1)]
