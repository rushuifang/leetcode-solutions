class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        length = {}
        for idx, point in enumerate(points):
            length[idx] = point[0] ** 2 + point[1] ** 2
        return [points[el[0]] for el in sorted(length.items(), key=lambda x: x[1])[:K]]
