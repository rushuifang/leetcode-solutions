class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, count = 0, 0
        while count < len(nums):
            if nums[i] == 2:
                del nums[i]
                nums.append(2)
                i -= 1
            elif nums[i] == 0:
                del nums[i]
                nums.insert(0, 0)
            i += 1
            count += 1
