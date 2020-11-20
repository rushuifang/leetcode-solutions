class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        self.backTr(k, n, [])
        return self.res
        
    def backTr(self, k, n, curr_sol):
        if k < 0 or n < 0:
            return
        if k == 0 and n == 0:
            self.res.append(curr_sol)
            
        if not curr_sol:
            start = 1
        else:
            start = curr_sol[-1] + 1
        
        for i in range(start, 10):
            self.backTr(k - 1, n - i, curr_sol + [i])