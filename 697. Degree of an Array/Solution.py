class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}
        for idx, num in enumerate(nums):
            if num not in left:
                left[num] = idx
            right[num] = idx
            count[num] = count.get(num, 0) + 1

        ans = len(nums)
        maxF = max(count.values())
        for num in count:
            if count[num] == maxF:
                ans = min(ans, right[num] - left[num] + 1)
        return ans