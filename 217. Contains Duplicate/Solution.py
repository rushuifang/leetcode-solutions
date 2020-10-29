class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        hash_table = {}
        for num in nums:
            hash_table[num] = hash_table.get(num, 0) + 1
        if sorted(hash_table.values(), reverse=True)[0] > 1:
            return True
        else:
            return False