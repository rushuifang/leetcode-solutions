class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        freq = {}
        
        for el in arr:
            if el not in freq:
                freq[el] = 1
            else:
                freq[el] += 1
            if freq[el] > n * 0.25:
                return el
            