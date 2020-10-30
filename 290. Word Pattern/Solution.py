class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        l = s.split(" ")
        if len(l) != len(pattern):
            return False
        hash_set = {}
        for i in range(len(pattern)):
            if pattern[i] not in hash_set:
                hash_set[pattern[i]] = l[i]
            else:
                if hash_set[pattern[i]] != l[i]:
                    return False
        if len(list(hash_set.values())) > len(set(hash_set.values())):
            return False
        return True