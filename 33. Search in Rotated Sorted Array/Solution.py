class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            m = (low + high) // 2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                if target > nums[high] and nums[m] < nums[high]:
                    high = m - 1
                else:
                    low = m + 1
            else:
                if target < nums[low] and nums[low] <= nums[m]:
                    low = m + 1
                else:
                    high = m - 1
        return -1