class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(maxsize=None)
        def dfs(n):
            if n == 0:
                return False
            sqrt_root = int(n ** 0.5)
            for i in range(1, sqrt_root + 1):
                if not dfs(n - i * i):
                    return True
            return False

        return dfs(n)