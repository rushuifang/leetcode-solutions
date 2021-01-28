import collections
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left, right = 0, 0
        letterDict = collections.Counter(p)
        required = len(letterDict)
        formed = 0
        window = {}
        res = []
        
        while right < len(s):
            newLetter = s[right]
            window[newLetter] = window.get(newLetter, 0) + 1
            if newLetter in letterDict and letterDict[newLetter] == window[newLetter]:
                formed += 1
            
            while formed == required:
                if right - left == len(p) - 1:
                    res.append(left)
                oldLetter = s[left]
                window[oldLetter] -= 1
                if oldLetter in letterDict and letterDict[oldLetter] > window[oldLetter]:
                    formed -= 1
                left += 1
            
            right += 1
        
        return res