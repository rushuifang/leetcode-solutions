class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def swap(i, j, L):
            temp = L[i]
            L[i] = L[j]
            L[j] = temp

        def reverse(nums, start):
            i = start
            j = len(nums) - 1
            while i < j:
                swap(i, j, nums)
                i += 1
                j -= 1

        i = len(nums) - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            swap(i, j, nums)
        reverse(nums, i + 1)
