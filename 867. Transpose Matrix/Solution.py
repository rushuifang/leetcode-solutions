class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        B = []
        m = len(A)
        n = len(A[0])
        
        for j in range(n):
            B.append([A[i][j] for i in range(m)])
        return B