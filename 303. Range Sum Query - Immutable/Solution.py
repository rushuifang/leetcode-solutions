class NumArray:
    def __init__(self, nums: List[int]):
        self.cuSum_list = [0]
        cuSum = 0
        for el in nums:
            cuSum += el
            self.cuSum_list.append(cuSum)

    def sumRange(self, i: int, j: int) -> int:
        if i > 0 and j > 0:
            return self.cuSum_list[j + 1] - self.cuSum_list[i]
        else:
            return self.cuSum_list[j + 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)