class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        t = float("inf")
        for i in range(len(timePoints) - 1, 0, -1):
            t = min(
                int(timePoints[i].split(":")[0]) * 60
                + int(timePoints[i].split(":")[1])
                - int(timePoints[i - 1].split(":")[0]) * 60
                - int(timePoints[i - 1].split(":")[1]),
                t,
            )
        t = min(
            24 * 60
            - int(timePoints[-1].split(":")[0]) * 60
            - int(timePoints[-1].split(":")[1])
            + int(timePoints[0].split(":")[0]) * 60
            + int(timePoints[0].split(":")[1]),
            t,
        )
        return t