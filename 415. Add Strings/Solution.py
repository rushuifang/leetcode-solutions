class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p = len(num1) - 1
        q = len(num2) - 1
        carry = 0
        res = []
        while p >= 0 or q >= 0:
            x1 = ord(num1[p]) - ord("0") if p >= 0 else 0
            x2 = ord(num2[q]) - ord("0") if q >= 0 else 0
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            res.append(value)
            p -= 1
            q -= 1
        if carry:
            res.append(carry)
        return "".join(str(el) for el in res[::-1])