class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_table = collections.defaultdict(list)
        for idx, num in enumerate(nums):
            # hash_table[num] += [idx]
            hash_table[num].append(idx)
        for el in hash_table.values():
            if len(el) > 1:
                for i in range(len(el) - 1):
                    if abs(el[i] - el[i + 1]) <= k:
                        return True
        return False