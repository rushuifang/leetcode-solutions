class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        b = [el for el in magazine]
        for el in ransomNote:
            if el not in b:
                return False
            else:
                b.remove(el)
        return True