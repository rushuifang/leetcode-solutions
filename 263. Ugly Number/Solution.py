class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        while num > 5:
            if not num % 2:
                num = num // 2
            if not num % 3:
                num = num // 3
            if not num % 5:
                num = num // 5
            if num % 2 and num % 3 and num % 5:
                break
        if num > 5:
            return False
        else:
            return True


class Solution(object):
    def isUgly(self, num):
        while num > 0:
            if num % 2 == 0:
                num = num // 2
            elif num % 3 == 0:
                num = num // 3
            elif num % 5 == 0:
                num = num // 5
            elif num == 1:
                return True
            else:
                return False
        return False
