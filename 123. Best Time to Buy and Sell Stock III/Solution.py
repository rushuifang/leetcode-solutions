class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        if days == 0:
            return 0
        num_transaction = 3
        dp = [[0 for _ in range(days)] for _ in range(num_transaction)]
        for transaction in range(1, num_transaction):
            maxdiff = -prices[0]
            for day in range(1, days):
                maxdiff = max(maxdiff, dp[transaction - 1][day - 1] - prices[day - 1])
                dp[transaction][day] = max(
                    dp[transaction][day - 1], prices[day] + maxdiff
                )
        return dp[-1][-1]