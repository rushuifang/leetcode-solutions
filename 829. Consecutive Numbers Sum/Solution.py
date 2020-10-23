class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        upper = math.floor(math.sqrt(2 * (N - 1) + 0.25) + 0.5)
        count = 0
        for k in range(1, upper + 1):
            if (N - (k - 1) * k * 0.5) % k == 0:
                count += 1
        return count