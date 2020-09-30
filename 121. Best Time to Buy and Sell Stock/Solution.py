# Greedy
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minPrice = prices[0]
        maxProf = 0
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            else:
                maxProf = max(maxProf, prices[i] - minPrice)
        return maxProf
