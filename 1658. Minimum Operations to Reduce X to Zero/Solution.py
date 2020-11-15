# My dfs with TLE
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        @lru_cache(None)
        def dfs(i, j, x, depth):
            if i > j or i > len(nums) - 1 or j < 0:
                return float("inf")
            if x - nums[i] == 0 or x - nums[j] == 0:
                return depth + 1
            return min(dfs(i + 1, j, x - nums[i], depth + 1), dfs(i, j - 1, x- nums[j], depth + 1))
        ans = dfs(0, len(nums) - 1, x, 0)
        if ans == float("inf"):
            return -1
        else:
            return ans

# Solution
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target == 0:
            return len(nums)
        
        map = {0:-1}
        preSum = 0
        res = 0
        for i in range(len(nums)):
            preSum += nums[i]
            if preSum - target in map:
                res = max(res, i - map[preSum - target])
            else:
                map[preSum] = i
        
        if res == 0:
            return -1
        else:
            return len(nums) - res