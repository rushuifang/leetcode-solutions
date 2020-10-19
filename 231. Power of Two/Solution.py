class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        else:
            return (n & n - 1) == 0


# following solution is too slow!
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n % 2 == 0:
            n //= 2
        return n == 1