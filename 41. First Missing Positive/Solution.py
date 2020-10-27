# My solution with O(1) space
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        nums = [el for el in nums if el > 0]
        if len(nums) == 0 or (len(nums) == 1 and nums[0] > 1):
            return 1
        if len(nums) == 1 and nums[0] == 1:
            return 2
        i = 1
        idx = 0
        while idx < len(nums) - 1:
            if nums[idx] == i and nums[idx] != nums[idx + 1]:
                i += 1
                idx += 1
            elif nums[idx] == i and nums[idx] == nums[idx + 1]:
                idx += 1
            else:
                return i
        if idx == len(nums) - 1 and nums[idx - 1] + 1 == nums[idx]:
            return nums[idx - 1] + 2
        elif idx == len(nums) - 1 and nums[idx - 1] + 1 != nums[idx]:
            return nums[idx - 1] + 1


# Easier code, but O(n) space
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # find the first missing positive number starting from 1 the first postive number and incrementing.
        # The first number not found in set is the first missing positive number.

        store = set([i for i in nums])
        start = 1
        while start in store:
            start += 1
        return start