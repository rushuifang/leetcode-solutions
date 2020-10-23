# TLE
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def jumpFromPosition(position, nums):
            if position == len(nums) - 1:
                return True
            furthurPosition = min(position + nums[position], len(nums) - 1)
            for i in range(furthurPosition, position, -1):
                if jumpFromPosition(i, nums):
                    return True
            return False

        return jumpFromPosition(0, nums)


# Greedy
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastPos = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] + i >= lastPos:
                lastPos = i
        return lastPos == 0