import math


class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        towers.sort(key=lambda x: x[0])
        maxQ = [float("-inf"), 0]
        for i in range(len(towers)):
            quality = 0
            for j in range(len(towers)):
                d = math.sqrt(
                    (towers[i][0] - towers[j][0]) ** 2
                    + (towers[i][1] - towers[j][1]) ** 2
                )
                if d > radius:
                    continue
                else:
                    quality += towers[j][2] // (1 + d)
            if quality > maxQ[0]:
                maxQ[0] = quality
                maxQ[1] = i
            elif quality == maxQ[0]:

                if towers[maxQ[1]][0] > towers[i][0]:
                    maxQ[1] == i
                elif towers[maxQ[1]][0] == towers[i][0]:
                    if towers[maxQ[1]][1] > towers[i][1]:
                        maxQ[1] == i

        return towers[maxQ[1]][:2]