class Solution:
    def reformat(self, s: str) -> str:
        letters = []
        numbers = []
        ans = ""
        for ch in s:
            if ch.isalpha():
                letters.append(ch)
            else:
                numbers.append(ch)
        if abs(len(letters) - len(numbers)) > 1:
            return ans
        else:
            if len(letters) > len(numbers):
                for i in range(len(numbers)):
                    ans += letters[i]
                    ans += numbers[i]
                ans += letters[-1]
                return ans
            elif len(letters) < len(numbers):
                for i in range(len(letters)):
                    ans += numbers[i]
                    ans += letters[i]
                ans += numbers[-1]
                return ans
            else:
                for i in range(len(numbers)):
                    ans += letters[i]
                    ans += numbers[i]
                return ans