class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        score, intermediate = 0, 0
        while tokens:
            if P >= tokens[0]:
                P -= tokens[0]
                score += 1
                tokens.pop(0)
            elif P < tokens[0] and score >= 1:
                P += tokens[-1]
                intermediate = score
                score -= 1
                tokens.pop()
            else:
                break
        if intermediate > score:
            return intermediate
        else:
            return score


# My solution is faster than 100% Python submissions! Yayyy
