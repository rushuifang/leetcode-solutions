# My unnecessary storage of two arrays
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        neg, pos = [], []
        i = 0
        while i < len(A):
            if A[i] < 0:
                neg.insert(0, A[i]*A[i])
                A.pop(i)
            elif A[i] >= 0:
                pos.append(A[i]*A[i])
                i += 1
            
        ans = []
        while neg and pos:
            if neg[0] <= pos[0]:
                ans.append(neg[0])
                neg.pop(0)
            else:
                ans.append(pos[0])
                pos.pop(0)
        if neg:
            return ans + neg
        if pos:
            return ans + pos
                
# Easier solution
class Solution(object):
    def sortedSquares(self, A):
        N = len(A)
        # i, j: negative, positive parts
        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1

        ans = []
        while 0 <= i and j < N:
            if A[i]**2 < A[j]**2:
                ans.append(A[i]**2)
                i -= 1
            else:
                ans.append(A[j]**2)
                j += 1

        while i >= 0:
            ans.append(A[i]**2)
            i -= 1
        while j < N:
            ans.append(A[j]**2)
            j += 1

        return ans