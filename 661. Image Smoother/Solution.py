class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        srdings = [[1, 0], [-1, 0], [1, 1], [1, -1], [0, 1], [0, -1], [-1, -1], [-1, 1],]
        m = len(M)
        n = len(M[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                cul_sum = M[i][j]
                num = 1
                for di, dj in srdings:
                    ii = i + di
                    jj = j + dj
                    if ii >= 0 and ii < m and jj >=0 and jj < n:
                        num += 1
                        cul_sum += M[ii][jj]
                ans[i][j] = cul_sum // num
        
        return ans