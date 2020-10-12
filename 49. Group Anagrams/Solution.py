class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = ["".join(sorted([ch for ch in el])) for el in strs]
        group = {}
        res = []
        for idx, el in enumerate(l):
            if el in group:
                group[el].append(idx)
            else:
                group[el] = [idx]
        for el in group.values():
            anagram = []
            for idx in el:
                anagram.append(strs[idx])
            res.append(anagram)
        return res


class Solution(object):
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()