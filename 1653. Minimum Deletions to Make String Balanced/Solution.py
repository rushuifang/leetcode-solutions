class Solution:
    def minimumDeletions(self, s: str) -> int:
        count = 0
        res = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "a":
                count += 1
            elif s[i] == "b":
                if count > 0:
                    count -= 1
                    res += 1
        return res