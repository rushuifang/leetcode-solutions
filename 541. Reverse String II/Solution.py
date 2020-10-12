class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = ""
        while len(s) >= 2 * k:
            ans += s[:k][::-1] + s[k : 2 * k]
            s = s[2 * k :]
        if len(s) < k:
            ans += s[::-1]
        else:
            ans += s[:k][::-1] + s[k:]
        return ans