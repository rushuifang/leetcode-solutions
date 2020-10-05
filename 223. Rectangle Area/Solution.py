class Solution:
    def computeArea(
        self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int
    ) -> int:
        if A <= E:
            x1 = E
        else:
            x1 = A
        if C <= G:
            x2 = C
        else:
            x2 = G
        if B <= F:
            y1 = F
        else:
            y1 = B
        if D <= H:
            y2 = D
        else:
            y2 = H
        if x1 >= x2 or y1 >= y2:
            overlap = 0
        else:
            overlap = (y2 - y1) * (x2 - x1)
        total = (C - A) * (D - B) + (G - E) * (H - F) - overlap
        return total