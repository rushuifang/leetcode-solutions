class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1,len(s)//2):
            s_copy = s
            while s_copy:
                if (s_copy[:i] == s_copy[i:2i]):
                    s_copy = s_copy[i:]
                else: 
                    return False
        return True

#  Correct solution:
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in s[1:]+s[:-1]