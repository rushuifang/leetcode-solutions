import collections


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        subStrs = collections.defaultdict(int)
        for i in range(len(s) - 9):
            subStrs[s[i : i + 10]] += 1
        return [subStr for subStr, num in subStrs.items() if num > 1]
