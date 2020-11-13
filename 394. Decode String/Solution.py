class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        freq = ""
        ans = ""
        for char in s:
            if char.isalpha():
                ans += char
            elif char.isdigit():
                freq += char
            elif char == "[":
                stack.append((ans, int(freq)))
                ans = ""
                freq = ""
            elif char == "]":
                pre, n = stack.pop()
                ans = pre + n*ans
        return ans