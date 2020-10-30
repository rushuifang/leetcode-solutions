class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_set = {}
        for num in nums:
            hash_set[num] = hash_set.get(num, 0) + 1
        hash_sort = sorted(hash_set.items(), key=lambda x: -x[1])
        ans = []
        for i in range(k):
            ans.append(hash_sort[i][0])
        return ans