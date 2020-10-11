class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_idx = {}
        current_res = []
        for idx, ch in enumerate(s):
            last_idx[ch] = idx
        for i, ch in enumerate(s):
            if ch not in current_res:
                while current_res and ch < current_res[-1] and i < last_idx[current_res[-1]]:
                    current_res.pop()
                current_res.append(ch)
        return "".join(current_res)