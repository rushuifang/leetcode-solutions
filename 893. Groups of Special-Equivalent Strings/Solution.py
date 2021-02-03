class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        def parityCount(word):
            ans = [0] * 52
            for idx, letter in enumerate(word):
                ans[ord(letter) - ord("a") + (idx % 2) * 26] += 1
            return tuple(ans)
        return len(set(parityCount(word) for word in A))
            