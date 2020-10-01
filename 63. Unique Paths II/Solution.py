class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row_num = len(obstacleGrid)
        col_num = len(obstacleGrid[0])
        for i in range(row_num):
            for j in range(col_num):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = "obs"
        if obstacleGrid[0][0] == "obs" or obstacleGrid[-1][-1] == "obs":
            return 0
        for i in range(row_num):
            if obstacleGrid[i][0] != "obs":
                obstacleGrid[i][0] = 1
        for j in range(col_num):
            if obstacleGrid[0][j] != "obs":
                obstacleGrid[0][j] = 1
        if "obs" in obstacleGrid[0]:
            col_idx = obstacleGrid[0].index("obs")
            for j in range(col_idx + 1, col_num):
                obstacleGrid[0][j] = 0
        first_col = [obstacleGrid[i][0] for i in range(row_num)]
        if "obs" in first_col:
            row_idx = first_col.index("obs")
            for i in range(row_idx + 1, row_num):
                obstacleGrid[i][0] = 0
        for i in range(1, row_num):
            for j in range(1, col_num):
                if obstacleGrid[i][j] != "obs":
                    if (
                        obstacleGrid[i - 1][j] != "obs"
                        and obstacleGrid[i][j - 1] != "obs"
                    ):
                        obstacleGrid[i][j] = (
                            obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                        )
                    elif (
                        obstacleGrid[i - 1][j] != "obs"
                        and obstacleGrid[i][j - 1] == "obs"
                    ):
                        obstacleGrid[i][j] = obstacleGrid[i - 1][j]
                    elif (
                        obstacleGrid[i - 1][j] == "obs"
                        and obstacleGrid[i][j - 1] != "obs"
                    ):
                        obstacleGrid[i][j] = obstacleGrid[i][j - 1]
                    else:
                        obstacleGrid[i][j] = 0
        return obstacleGrid[-1][-1]


# Simplified version
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        # If the starting cell has an obstacle, then simply return as there would be
        # no paths to the destination.
        if obstacleGrid[0][0] == 1:
            return 0

        # Number of ways of reaching the starting cell = 1.
        obstacleGrid[0][0] = 1

        # Filling the values for the first column
        for i in range(1,m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

        # Filling the values for the first row        
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)

        # Starting from cell(1,1) fill up the values
        # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
        # i.e. From above and left.
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 0:
                     obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0

        # Return value stored in rightmost bottommost cell. That is the destination.            
        return obstacleGrid[m-1][n-1]