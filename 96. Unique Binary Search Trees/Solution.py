class Solution:
    def numTrees(self, n: int) -> int:
        G = [1, 1]
        for j in range(2, n + 1):
            sumG = 0
            for i in range(1, j + 1):
                F = G[i - 1] * G[j - i]
                sumG += F
            G.append(sumG)
        return G[n]
