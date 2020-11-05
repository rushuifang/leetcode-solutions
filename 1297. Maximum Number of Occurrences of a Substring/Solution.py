class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        count = collections.Counter()
        for i in range(len(s) - minSize + 1):
            subStr = s[i : i + minSize]
            if len(set(subStr)) <= maxLetters:
                count[subStr] += 1

        if count:
            return max(count.values())
        return 0