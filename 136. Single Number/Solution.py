class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_set = collections.defaultdict(int)
        for el in nums:
            hash_set[el] += 1
        return sorted(hash_set.items(), key=lambda x: x[1])[0][0]


# math
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)


# bit manipulation
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a