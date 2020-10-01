class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split(" ")
        while l:
            if l[-1] == "":
                del l[-1]
            else:
                break
        if l:
            return len(l[-1])
        else:
            return 0