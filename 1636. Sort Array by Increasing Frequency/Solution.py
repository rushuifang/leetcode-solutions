class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        hash_set = {}
        for num in nums:
            hash_set[num] = hash_set.get(num, 0) + 1
        ans = []
        for el in sorted(hash_set.items(), key=lambda x: (x[1], -x[0])):
            ans += [el[0]] * el[1]
        return ans