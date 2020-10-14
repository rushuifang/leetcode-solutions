class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        r1 = int(a.split("+")[0])
        i1 = int(a.split("+")[1][:-1])
        r2 = int(b.split("+")[0])
        i2 = int(b.split("+")[1][:-1])
        r = r1 * r2 - i1 * i2
        i = r1 * i2 + r2 * i1
        return str(r) + "+" + str(i) + "i"
