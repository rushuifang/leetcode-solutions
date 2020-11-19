class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        prevRow = [1]
        
        def recursive(prevRow):
            n = len(prevRow) + 1
            Row = [1 for _ in range(n)]
            for i in range(1, n - 1):
                Row[i] = prevRow[i - 1] + prevRow[i]
            return Row
        
        for i in range(rowIndex):
            prevRow = recursive(prevRow)
        
        return prevRow