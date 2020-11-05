class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(" ")
        maxWordLen = 0
        for word in words:
            maxWordLen = max(maxWordLen, len(word))
        for i in range(len(words)):
            words[i] += (maxWordLen - len(words[i])) * " "
        ans = [""] * maxWordLen

        for i in range(maxWordLen):
            for word in words:
                ans[i] += word[i]
            ans[i] = ans[i].rstrip()
        return ans
