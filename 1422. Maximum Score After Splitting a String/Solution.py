class Solution:
    def maxScore(self, s: str) -> int:
        maxScore = int(s[0] == "0") + sum(int(el) for el in s[1:])
        temp = int(s[0] == "0") + sum(int(el) for el in s[1:])

        for i in range(1, len(s) - 1):
            if s[i] == "0":
                temp += 1
            else:
                temp -= 1
            maxScore = max(maxScore, temp)
        return maxScore