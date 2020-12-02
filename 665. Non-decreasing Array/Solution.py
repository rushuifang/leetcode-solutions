class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        for i in range(n - 1):
            if nums[i] > nums[i + 1] and (i == n - 2 or nums[i + 2] >= nums[i]):
                count += 1
                nums[i + 1] = nums[i]
            elif nums[i] > nums[i + 1] and (i == 0 or nums[i - 1] <= nums[i + 1]):
                count += 1
                nums[i] = nums[i + 1]
            elif nums[i] > nums[i + 1] and (i == n - 2 or nums[i + 2] < nums[i]) and (i == 0 or nums[i - 1] > nums[i + 1]):
                return False
            if count > 1:
                return False
        return True