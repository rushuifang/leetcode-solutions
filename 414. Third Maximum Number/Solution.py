# stack
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        stack1 = []
        stack2 = []
        
        for num in nums:
            while stack1 and stack1[-1] < num:
                stack2.append(stack1.pop())
            if len(stack1) < 3 and num not in stack1:
                stack1.append(num)
            while stack2 and len(stack1) < 3:
                stack1.append(stack2.pop())
                
        if len(stack1) < 3:
            return stack1[0]
        else:
            return stack1[-1]
            
# set
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        nums -= {max(nums)}
        nums -= {max(nums)}
        return max(nums)