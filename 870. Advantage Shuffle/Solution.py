class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        sortedA = sorted(A)
        sortedB = sorted(B)
        assigned = {b: [] for b in B}
        remaining = []
        j = 0
        
        for a in sortedA:
            if a > sortedB[j]:
                assigned[sortedB[j]].append(a)
                j += 1
            else:
                remaining.append(a)
        
        ans = []
        for b in B:
            if assigned[b]:
                ans.append(assigned[b].pop())
            else:
                ans.append(remaining.pop())
        return ans