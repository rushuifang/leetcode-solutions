class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        n = len(arr)
        k = int(0.05 * n)
        return sum(arr[k:-k]) / (0.9 * n)
