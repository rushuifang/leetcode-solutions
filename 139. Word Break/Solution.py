class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]


# Hints: Dynamic programming, bottom up. dp[i] is if s[0:i] is breakable.
# if dp[j] is true and s[j:i] is in wordDict, then dp[i] is breakable too.