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

# stack
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0 for _ in range(len(T))]
        stack = []
        
        for i in range((len(T) - 1), -1, -1):
            while stack and T[stack[-1]] <= T[i]:
                stack.pop()
            if stack == []:
                res[i] = 0
            else:
                res[i] = stack[-1] - i
            stack.append(i)
        
        return res