class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            if s[i] in t:
                t = t[t.index(s[i]) + 1 :]
            else:
                return False
        return True