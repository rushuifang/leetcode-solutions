class Solution:
    def judgeCircle(self, moves: str) -> bool:
        r = moves.count("R")
        l = moves.count("L")
        u = moves.count("U")
        d = moves.count("D")
        if r == l and u == d:
            return True
        return False
