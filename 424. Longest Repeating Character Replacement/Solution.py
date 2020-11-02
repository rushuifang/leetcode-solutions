class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chfreq = defaultdict(int)
        maxLen,maxFreq = 0, 0
        start, end = 0, 0
        
        while end < len(s):
            chfreq[s[end]] += 1
            maxFreq = max(maxFreq, chfreq[s[end]])
            
            if maxFreq + k < end - start + 1:
                chfreq[s[start]] -= 1
                start += 1
            else:
                maxLen = max(maxLen, end - start + 1)
            end += 1
            
        return maxLens