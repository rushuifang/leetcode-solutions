class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        for _ in range(len(A)):
            if A[i] % 2 == 0:
                i += 1
            else:
                A.append(A.pop(i))
        return A