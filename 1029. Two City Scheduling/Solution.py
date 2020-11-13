class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)//2
        diff = [a - b for (a, b) in costs]
        sorted_diff = sorted((value, idx) for idx, value in enumerate(diff))
        min_cost = 0
        for i in range(n):
            min_cost += costs[sorted_diff[i][1]][0]
        for i in range(n, 2*n):
            min_cost += costs[sorted_diff[i][1]][1]
        return min_cost