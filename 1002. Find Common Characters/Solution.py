class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = [letter for letter in A[0]]
        
        for i in range(1, len(A)):
            cache = []
            for letter in A[i]:
                if letter in res:
                    res.remove(letter)
                    cache.append(letter)
            res = cache
        return res
        