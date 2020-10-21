class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        numsSort = sorted(nums)
        if numsSort[-1] >= 2 * numsSort[-2]:
            return nums.index(numsSort[-1])
        else:
            return -1


# if there are multiple largest nums
class Solution(object):
    def dominantIndex(self, nums):
        m = max(nums)
        if all(m >= 2 * x for x in nums if x != m):
            return nums.index(m)
        return -1