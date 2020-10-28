class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftmax, rightmax = 0, 0
        water = 0

        while left < right:
            if leftmax < height[left]:
                leftmax = height[left]
            if rightmax < height[right]:
                rightmax = height[right]
            if leftmax < rightmax:
                water += max(0, leftmax - height[left])
                left += 1
            else:
                water += max(0, rightmax - height[right])
                right -= 1
        return water