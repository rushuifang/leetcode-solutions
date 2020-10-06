class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        idx = 0
        while idx < len(intervals) - 1:
            if intervals[idx][1] >= intervals[idx + 1][0]:
                if intervals[idx][1] >= intervals[idx + 1][1]:
                    intervals.pop(idx + 1)
                else:
                    intervals[idx][1] = intervals[idx + 1][1]
                    intervals.pop(idx + 1)
            else:
                idx += 1
        return intervals