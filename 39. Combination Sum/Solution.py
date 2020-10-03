class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backTr(target, combination, k):
            if target == 0:
                sol.append(combination)
            if target < 0 or k > len(candidates):
                return
            for i in range(k, len(candidates)):
                backTr(target - candidates[i], combination + [candidates[i]], i)

        sol = []
        backTr(target, [], 0)
        return sol