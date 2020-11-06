class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            res += [sorted(curr + [num]) for curr in res if sorted(curr + [num]) not in res]
        return res