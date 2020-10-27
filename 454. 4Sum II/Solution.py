class Solution:
    def fourSumCount(
        self, A: List[int], B: List[int], C: List[int], D: List[int]
    ) -> int:
        dic1 = self.helper(A, B)
        dic2 = self.helper(C, D)
        res = 0

        for sum1 in dic1:
            if -sum1 in dic2:
                res += dic1[sum1] * dic2[-sum1]
        return res

    def helper(self, l1, l2):
        dic = collections.defaultdict(int)
        for a in l1:
            for b in l2:
                dic[a + b] += 1
        return dic