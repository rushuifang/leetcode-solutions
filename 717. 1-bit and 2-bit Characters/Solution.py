class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        while len(bits) > 1:
            if bits[0] == 0:
                bits.pop(0)
            elif bits[0] == 1:
                bits.pop(0)
                bits.pop(0)
        if len(bits) == 1:
            return True
        else:
            return False
