class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        odd = 0
        even = 0
        for i in range(len(piles)):
            if i % 2 == 0:
                even += piles[i]
            else:
                odd += piles[i]
        return odd > even or even > odd

# so... just return True