class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        codes = code + code + code
        n = len(code)
        ans = [0 for _ in range(n)]
        if k == 0:
            return ans
        elif k > 0:
            for i in range(n):
                ans[i] = sum(codes[n+i+1:n+i+1+k])
        elif k < 0:
            for i in range(n):
                ans[i] = sum(codes[n+i-abs(k):n+i])
        return ans