class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq = {}
        i = 0
        
        while i < len(nums):
            if nums[i] not in freq:
                freq = {}
                freq[nums[i]] = 1
                i += 1
            else:
                freq[nums[i]] += 1
                if freq[nums[i]] > 2:
                    nums.pop(i)
                else:
                    i += 1
        return len(nums)