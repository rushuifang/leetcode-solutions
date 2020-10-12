class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = str(n)
        if len(s) == 1:
            return -1
        for i in range(len(s) - 1, 0, -1):
            if s[i] <= s[i - 1] and i != 1:
                continue
            elif s[i] <= s[i - 1] and i == 1:
                return -1
            else:
                a = sorted(s[i:])
                idx = 0
                while idx < len(a):
                    if a[idx] > s[i - 1]:
                        break
                    else:
                        idx += 1
                res1 = s[:i] + "".join(sorted(a))
                res = (
                    res1[: i - 1]
                    + res1[i + idx]
                    + res1[i : i + idx]
                    + res1[i - 1]
                    + res1[i + idx + 1 :]
                )
                return int(res) if int(res) < 2 ** 31 - 1 else -1
