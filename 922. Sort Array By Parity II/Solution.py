class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = 0
        j = 1
        ans = [0 for _ in range(len(A))]
        for num in A:
            if num % 2 == 0:
                ans[i] = num
                i += 2
            else:
                ans[j] = num
                j += 2
        return ans