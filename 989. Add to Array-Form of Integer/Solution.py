class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        B = [int(char) for char in str(K)]
        
        carry = 0
        flag = 0
        i = -1
        C = []
        
        while flag < len(A) and flag < len(B):
            flag += 1
            value = (A[i] + B[i] + carry) % 10
            carry = (A[i] + B[i] + carry) // 10
            C.insert(0, value)
            i -= 1
        if flag == len(A):
            while flag < len(B):
                flag += 1
                value = (B[i] + carry) % 10
                carry = (B[i] + carry) // 10
                C.insert(0, value)
                i -= 1
        elif flag == len(B):
            while flag < len(A):
                flag += 1
                value = (A[i] + carry) % 10
                carry = (A[i] + carry) // 10
                C.insert(0, value)
                i -= 1
        if carry == 1:
            C.insert(0, carry)
        return C