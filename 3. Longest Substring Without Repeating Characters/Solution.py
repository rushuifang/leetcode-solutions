class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        window = {}
        res = 0
        
        while right < len(s):
            newLetter = s[right]
            window[newLetter] = window.get(newLetter, 0) + 1
            right += 1
            
            while window[newLetter] > 1:
                oldLetter = s[left]
                window[oldLetter] -= 1
                left += 1
            res = max(res, right - left)
            
        return res
            