class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        s1 = s[::-1]
        l = []
        s = [el for el in s]
        for el in s1:
            if el in vowels:
                l.append(el)
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = l.pop(0)
        return "".join(s)
