class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        ans = maxNum = 0
        for idx, num in enumerate(arr):
            maxNum = max(maxNum, num)
            if idx == maxNum:
                ans += 1
        return ans