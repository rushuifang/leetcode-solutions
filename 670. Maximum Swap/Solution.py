class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        ans = num
        
        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                A = digits[:]
                A[i], A[j] = A[j], A[i]
                if int("".join(A)) > ans:
                    ans = int("".join(A))
        return ans