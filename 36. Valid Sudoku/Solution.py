class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [{} for _ in range(9)]
        col = [{} for _ in range(9)]
        box = [{} for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    num = int(num)
                    boxIdx = (i // 3) * 3 + j // 3
                    row[i][num] = row[i].get(num, 0) + 1
                    col[j][num] = col[j].get(num, 0) + 1
                    box[boxIdx][num] = box[boxIdx].get(num, 0) + 1
                    if row[i][num] > 1 or col[j][num] > 1 or box[boxIdx][num] > 1:
                        return False
        return True