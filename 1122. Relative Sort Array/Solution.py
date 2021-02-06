class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mapping = {}
        for idx, el in enumerate(arr2):
            mapping[el] = idx
        
        res1 = [[] for _ in range(len(arr2))]
        res2 = []
        res = []
        for el in arr1:
            if el in mapping:
                res1[mapping[el]].append(el)
            else:
                res2.append(el)
        
        for l in res1:
            for el in l:
                res.append(el)
        return res + sorted(res2)


# Better one
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import Counter
        elements = Counter(arr1)
        res = []
        
        for el in arr2:
            res += [el]*elements[el]
        for el in sorted(list(set(arr1) - set(arr2))):
            res += [el]*elements[el]
        
        return res