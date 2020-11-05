class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c = r = o = a = k = maxFrog = presentFrog = 0

        for ch in croakOfFrogs:
            if ch == "c":
                c += 1
                presentFrog += 1
            elif ch == "r":
                r += 1
            elif ch == "o":
                o += 1
            elif ch == "a":
                a += 1
            elif ch == "k":
                k += 1
                presentFrog -= 1
            if c < r or r < o or o < a or a < k:
                return -1
            maxFrog = max(maxFrog, presentFrog)

        if presentFrog == 0 and c == r == o == a == k:
            return maxFrog
        return -1
