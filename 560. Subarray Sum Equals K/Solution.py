class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = 0
        for start in range(len(nums)):
            cuSum = 0
            for end in range(start, len(nums)):
                cuSum += nums[end]
                if cuSum == k:
                    counts += 1
        return counts

    # For the same cumulative sum algorithm.
    # Python would not pass the submission because it's too slow, but Java can.

    class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cuSum = 0
        counts = 0
        hash_table = {}
        for i in range(len(nums)):
            if cuSum not in hash_table:
                hash_table[cuSum] = 1
            else:
                hash_table[cuSum] += 1
            cuSum += nums[i]
            if (cuSum-k) in hash_table:
                counts += hash_table[cuSum-k]
        return counts

        # Using hash map, complexity is O(n).