class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]


# Hints: If dp[i-1] means nums[i-1] is robbed, so you can't rob the next house
# nums[i]. Then dp[i] equals to either dp[i-1] or dp[i-2]+nums[i];
# However, if dp[i-1] doesn't mean nums[i-1] is robbed, you can rob nums[i], you'll have
# dp[i] equals to dp[i-1]+nums[i] or dp[i-1], where dp[i-1]+nums=dp[i-2]+nums.