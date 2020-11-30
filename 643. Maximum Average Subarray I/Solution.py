class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])
        curr_sum = sum(nums[:k])
        
        for i in range(len(nums) - k):
           
            curr_sum -= nums[i] 
            curr_sum += nums[i + k]
            max_sum = max(max_sum, curr_sum)
            
        return max_sum / k
            