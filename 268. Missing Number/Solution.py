class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        suppose_sum = (1 + n) * n // 2
        return suppose_sum - sum(nums)