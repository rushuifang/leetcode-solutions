class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        N = len(nums)
        if N == 1:
            return nums[0]
        if N % 2 == 0:
            return (nums[N//2-1]+nums[N//2])/2
        else:
            return nums[N//2]
        