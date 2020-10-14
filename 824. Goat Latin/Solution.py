class Solution:
    def toGoatLatin(self, S: str) -> str:
        ans = []
        for idx, char in enumerate(S.split(" ")):
            if char[0].lower() in ["a", "e", "i", "o", "u"]:
                char += "ma"
            else:
                char = char[1:] + char[0] + "ma"
            char += "a" * (idx + 1)
            ans.append(char)
        return " ".join(ans)
