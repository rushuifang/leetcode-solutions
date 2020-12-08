class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        nxt = [float("inf") for _ in range(102)]
        ans = [0] * len(T)
        
        for i in range(len(T) - 1, -1, -1):
            idx = min(nxt[t] for t in range(T[i] + 1, 102))
            if idx < float("inf"):
                ans[i] = idx - i
            nxt[T[i]] = i
        return ans