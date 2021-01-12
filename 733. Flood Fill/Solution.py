class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        oldColor = image[sr][sc]
        if oldColor == newColor: return image
        
        def dfs(r, c):
            image[r][c] = newColor
            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                rr = dr + r
                cc = dc + c
                if 0 <= rr < m and 0 <= cc < n and image[rr][cc] == oldColor:
                    dfs(rr, cc)
                    
        dfs(sr, sc)
        return image

# if oldColor == newColor: return image  If you didn't think of this edge case,
# you would go into an infinite loop!