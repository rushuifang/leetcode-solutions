class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        t_dict = collections.Counter(t)
        required = len(t_dict)
        formed = 0
        window_dict = {}
        left, right = 0, 0
        ans = float("inf"), None, None
        
        while right < len(s):
            char = s[right]
            window_dict[char] = window_dict.get(char, 0) + 1
            if char in t_dict and window_dict[char] == t_dict[char]:
                formed += 1
            
            while formed == required:
                if right - left + 1 < ans[0]:
                    ans = right - left + 1, left, right
                char = s[left]
                window_dict[char] -= 1
                if char in t_dict and window_dict[char] < t_dict[char]:
                    formed -= 1
                left += 1
            
            right += 1
        return s[ans[1]:ans[2]+1] if ans[0] != float("inf") else ""