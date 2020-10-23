class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        ans = []
        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)
                break
            elif i == len(nums) - 1:
                ans.append(-1)
        if ans[0] == -1:
            return [-1, -1]
        else:
            for j in range(len(nums) - 1, -1, -1):
                if nums[j] == target:
                    ans.append(j)
                    break
            return ans


# Solution provided by Leetcode:
# 1. linear scan
class Solution:
    def searchRange(self, nums, target):
        # find the index of the leftmost appearance of `target`. if it does not
        # appear, return [-1, -1] early.
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break
        else:
            return [-1, -1]

        # find the index of the rightmost appearance of `target` (by reverse
        # iteration). it is guaranteed to appear.
        for j in range(len(nums) - 1, -1, -1):
            if nums[j] == target:
                right_idx = j
                break

        return [left_idx, right_idx]


# 2. binary search
class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid + 1

        return lo

    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False) - 1]
