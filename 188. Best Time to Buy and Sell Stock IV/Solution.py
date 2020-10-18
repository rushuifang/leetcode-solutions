class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0 or k == 0:
            return 0

        if 2 * k > len(prices):
            res = 0
            for i, j in zip(prices[1:], prices[:-1]):
                res += max(0, i - j)
            return res

        dp = [[0 for _ in range(len(prices))] for _ in range(k + 1)]
        for transaction in range(1, 1 + k):
            maxdiff = -prices[0]
            for day in range(1, len(prices)):
                maxdiff = max(dp[transaction - 1][day - 1] - prices[day - 1], maxdiff)
                dp[transaction][day] = max(
                    dp[transaction][day - 1], prices[day] + maxdiff
                )
        return dp[-1][-1]