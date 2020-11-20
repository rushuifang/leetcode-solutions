class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = 0
        cur_min = 0
        ans = float("-inf")
        
        for num in nums:
            if num > 0:
                cur_max, cur_min = max(num, num * cur_max), min(num, num * cur_min)
            else:
                cur_max, cur_min = max(num, num * cur_min), min(num, num * cur_max)
            ans = max(cur_max, ans)
        if ans:
            return ans
        else:
            return max(nums)