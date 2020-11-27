class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        row = len(nums)
        col = len(nums[0])
        if r * c != row * col:
            return nums
        
        row_traverse = []
        for i in range(row):
            row_traverse += nums[i]

        out = []
        for i in range(r):
            out.append(row_traverse[i * c: (i + 1) * c])
        
        return out