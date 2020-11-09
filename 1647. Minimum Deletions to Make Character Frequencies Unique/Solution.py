class Solution:
    def minDeletions(self, s: str) -> int:
        freq = collections.defaultdict(int)
        for ch in s:
            freq[ch] += 1
        freqValues = list(freq.values())
        
        freqSet = set()
        res = 0
        while freqValues:
            t = freqValues.pop(0)
            while t in freqSet and t != 0:
                t -= 1
                res += 1
            if t != 0:
                freqSet.add(t)
        return res
            