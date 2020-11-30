class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sort_nums = sorted(nums)
        if sort_nums == nums:
            return 0
        idx = []
        for i in range(len(nums)):
            if nums[i] != sort_nums[i]:
                idx.append(i)
        return idx[-1] - idx[0] + 1