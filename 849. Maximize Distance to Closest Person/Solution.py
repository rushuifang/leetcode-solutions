class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        idx = seats.index(1)
        maxL = seats.index(1)
        n = len(seats)

        for i in range(seats.index(1) + 1, n):
            if seats[i] == 1 and i - idx > maxL:
                maxL = i - idx
                idx = i
            elif seats[i] == 1 and i - idx <= maxL:
                idx = i
        if maxL // 2 < n - 1 - idx and seats.index(1) < n - 1 - idx:
            return n - 1 - idx
        elif maxL // 2 < seats.index(1):
            return seats.index(1)
        else:
            return maxL // 2
