class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        newNums = nums + nums[:-1]
        result = []
        mapping = collections.defaultdict(list)
        stack= [nums[0]]
        
        for i in range(1, len(newNums)):
            while stack and stack[-1] < newNums[i]:
                mapping[stack[-1]].append(newNums[i])
                stack.pop()
            stack.append(newNums[i])
            
        for el in nums:
            if el in mapping:
                result.append(mapping[el].pop(0))
            else:
                result.append(-1)
        
        return result