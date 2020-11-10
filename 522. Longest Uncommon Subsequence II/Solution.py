class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        counter = Counter(strs)
        s = sorted(counter.keys(), key=len, reverse=True)

        def isSub(a, b):
            i, j = 0, 0
            while i < len(a) and j < len(b):
                if a[i] == b[j]:
                    i += 1
                j += 1
            return i == len(a)

        for i in range(len(s)):
            if counter[s[i]] > 1:
                continue
            if i == 0 or not any(isSub(s[i], s[j]) for j in range(i)):
                return len(s[i])
        return -1
