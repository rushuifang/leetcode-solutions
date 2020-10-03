class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d = {}
        for el in nums:
            if el not in d:
                d[el] = 1
            else:
                d[el] += 1
        if k:
            res = sum(el + k in d for el in d.keys())
        else:
            res = sum(el > 1 for el in d.values())
        return res