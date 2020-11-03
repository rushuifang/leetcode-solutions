class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        l = [[a, b] for a,b in zip(ages, scores)]
        l.sort(reverse=True)
        
        ans = 0
        dp = [0]*n
        
        for i in range(n):
            score = l[i][1]
            dp[i] = score
            for j in range(i):
                if l[j][1] >= score:
                    dp[i] = max(dp[i], dp[j] + score)
            ans = max(ans, dp[i])
        return ans