class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while i < len(nums) and j < len(nums):
            j += 1
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
            else:
                i += 1