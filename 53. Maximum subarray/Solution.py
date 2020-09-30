class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        newNum = nums[0]
        maxTotal = nums[0]
        for i in range(1, len(nums)):
            newNum = max(newNum + nums[i], nums[i])
            maxTotal = max(newNum, maxTotal)
        return maxTotal
