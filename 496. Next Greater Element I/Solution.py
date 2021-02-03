class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        stack = []
        result = []
        
        stack.append(nums2[0])
        for i in range(1, len(nums2)):
            while stack and stack[-1] < nums2[i]:
                mapping[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
        
        for i in range(len(nums1)):
            if nums1[i] in mapping:
                result.append(mapping[nums1[i]])
            else:
                result.append(-1)
        
        return result


# Enter stack reversely
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        stack = []
        result = []
        
        for i in range((len(nums2) - 1), -1, -1):
            while stack and stack[-1] < nums2[i]:
                stack.pop()
            if stack == []:
                mapping[nums2[i]] = -1
            else:
                mapping[nums2[i]] = stack[-1]
            stack.append(nums2[i])
        
        for el in nums1:
            result.append(mapping[el])
        
        return result