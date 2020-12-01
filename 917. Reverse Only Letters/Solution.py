class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        letters = ""
        for ch in S:
            if ch.isalpha():
                letters += ch
        letters = letters[::-1]
        
        for i in range(len(S)):
            if not S[i].isalpha():
                letters = letters[:i] + S[i] + letters[i:]
        return letters