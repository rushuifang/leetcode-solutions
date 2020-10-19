class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        factor = factorial(n - 1)
        ans = []
        nums = [i for i in range(1, n + 1)]
        
        for m in range(n - 1, 0, -1):
            idx = k // factor
            ans.append(str(nums.pop(idx)))
            k = k % factor
            factor = factor // m
        ans += [str(nums[0])]
        return "".join(ans)