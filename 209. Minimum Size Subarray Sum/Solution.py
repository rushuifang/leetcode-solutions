class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        cuSum = 0
        left = 0
        res = len(nums) + 1
        for i in range(len(nums)):
            cuSum += nums[i]
            while cuSum >= s:
                res = min(res, i - left + 1)
                cuSum -= nums[left]
                left += 1
        if res < len(nums) + 1:
            return res
        else:
            return 0
