# O(N)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]

        i = 0
        while i < len(nums) - 1:
            if nums[i] < nums[i + 1]:
                i += 1
            else:
                return nums[i + 1]

# O(log(N))
class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid + 1
        return nums[low]