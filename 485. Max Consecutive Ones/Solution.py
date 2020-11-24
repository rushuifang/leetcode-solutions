class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one = 0
        cur_one = 0
        
        for num in nums:
            if cur_one == 0 and num == 1:
                cur_one = 1
            elif cur_one != 0 and num == 1:
                cur_one += 1
            elif cur_one != 0 and num == 0:
                max_one = max(max_one, cur_one)
                cur_one = 0
                
        return max(max_one, cur_one)