class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_set = {")":"(", "}":"{", "]":"["}
        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)
            else:
                if stack and hash_set[ch] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
        return not stack