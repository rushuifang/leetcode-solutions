class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            index = abs(nums[i]) - 1
            if nums[index] > 0:
                nums[index] = - nums[index]
            else:
                dup = index + 1
                
        for i in range(n):
            if nums[i] > 0:
                missing = i + 1
        
        return [dup, missing]