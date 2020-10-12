class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) or len(A) < 2 or len(B) < 2:
            return False
        uncommon = []
        for idx in range(len(A)):
            if A[idx] != B[idx]:
                uncommon.append(idx)
        if len(uncommon) == 2:
            if A[uncommon[0]] == B[uncommon[1]] and A[uncommon[1]] == B[uncommon[0]]:
                return True
        elif len(uncommon) == 0:
            if len(set(A)) < len(A):
                return True
        return False