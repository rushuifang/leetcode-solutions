class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for idx in range(len(s) // 2):
            s[idx], s[~idx] = s[~idx], s[idx]


# Or just use s.reverse()