class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        if n == 2:
            return 0
        odd, even = 0, 0
        res = 0
        for i in range(1, n):
            if i % 2 == 0:
                even += nums[i]
            else:
                odd += nums[i]
        if odd == even:
            res += 1
            
        for i in range(1, n):
            if i % 2 != 0:
                odd += nums[i - 1] - nums[i]
                if odd == even:
                    res += 1
            else:
                even += nums[i - 1] - nums[i]
                if odd == even:
                    res += 1
        return res