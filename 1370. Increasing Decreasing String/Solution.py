class Solution:
    def sortString(self, s: str) -> str:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        freqlist = [[a, b] for (a, b) in sorted(freq.items())]
        ans = ""
        while len(ans) < len(s):
            for i in range(len(freqlist)):
                if freqlist[i][1] != 0:
                    ans += freqlist[i][0]
                    freqlist[i][1] -= 1
            for i in range(len(freqlist) - 1, -1, -1):
                if freqlist[i][1] != 0:
                    ans += freqlist[i][0]
                    freqlist[i][1] -= 1
        return ans