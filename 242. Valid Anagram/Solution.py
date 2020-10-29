class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = [0 for _ in range(26)]
        for i in range(len(s)):
            counter[ord(s[i]) - ord("a")] += 1
            counter[ord(t[i]) - ord("a")] -= 1
        for el in counter:
            if el != 0:
                return False
        return True