class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backTrack(path, idx):
            if len(path) == k:
                result.append(path[:])
            
            for i in range(idx, n + 1):
                path.append(i)
                backTrack(path, i + 1)
                path.pop()
        
        result = []
        backTrack([], 1)
        return result
    