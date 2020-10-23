class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        stack = []
        mini = [nums[0] for i in range(len(nums))]
        for i in range(1, len(nums)):
            mini[i] = min(mini[i - 1], nums[i])
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] > mini[j]:
                while stack and stack[-1] <= mini[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        return False