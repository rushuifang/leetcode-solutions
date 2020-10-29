class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_table = {}
        for i in range(len(s)):
            if s[i] not in hash_table:
                hash_table[s[i]] = t[i]
            else:
                if hash_table[s[i]] != t[i]:
                    return False
        if len(list(hash_table.values())) > len(set(hash_table.values())):
            return False
        return True