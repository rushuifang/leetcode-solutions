# O(N^2)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        freq = len(nums) // 3 
        for num in nums:
            if num not in res and nums.count(num) > freq:
                res.append(num)
        return res

# O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k = 2
        candidates = {}
        
        for num in nums:
            if num in candidates:
                candidates[num] += 1
            elif len(candidates) < k:
                candidates[num] = 1
            else:
                temp = {}
                for c in candidates:
                    candidates[c] -= 1
                    if candidates[c] > 0:
                        temp[c] = candidates[c]
                candidates = temp
        
        res = [c for c in candidates if nums.count(c) > len(nums) // 3]
        return res