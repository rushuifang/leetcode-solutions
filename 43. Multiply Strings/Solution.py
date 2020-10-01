class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if len(num1) == 0 or len(num2) == 0:
            return "0"
        if num1 == "0" or num2 == "0":
            return "0"
        res1, res2 = 0, 0
        for d in num1:
            res1 = 10 * res1 + (ord(d) - ord("0"))
        for d in num2:
            res2 = 10 * res2 + (ord(d) - ord("0"))
        res = res1 * res2
        s = ""
        while res:
            s += chr(res % 10 + ord("0"))
            res = res // 10
        return s[::-1]