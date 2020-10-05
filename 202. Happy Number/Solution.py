class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        storage = [n]
        while n != "1":
            newN = 0
            for el in n:
                newN += int(el) ** 2
            n = str(newN)
            if n in storage:
                return False
            else:
                storage.append(n)
        return True