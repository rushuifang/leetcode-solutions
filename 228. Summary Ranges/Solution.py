class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        n = len(nums)
        i, j = 0, 1
        while i < n:
            j = 1
            while i + j < n and nums[i] + j == nums[i + j]:
                j += 1
            if j > 1:
                ans.append(str(nums[i]) + "->" + str(nums[i + j - 1]))
            else:
                ans.append(str(nums[i]))
            i += j
        return ans