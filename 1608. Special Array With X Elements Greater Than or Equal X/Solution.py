class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for x in range(1, len(nums) + 1):
            if (x != len(nums) and nums[x - 1] >= x and nums[x] < x) or (
                x == len(nums) and nums[x - 1] >= x
            ):
                return x
        return -1