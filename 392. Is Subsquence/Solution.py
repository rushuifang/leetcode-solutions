class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            if s[i] in t:
                t = t[t.index(s[i]) + 1 :]
            else:
                return False
        return True

# Follow up
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def binary(target, arr):
            low = 0
            high = len(arr)
            while low < high:
                mid = (low + high) // 2
                if arr[mid] >= target:
                    high = mid
                else:
                    low = mid + 1
            return low
        
        index = collections.defaultdict(list)
        for idx, char in enumerate(t) :
            index[char].append(idx)
            
        j = 0
        for char in s:
            if char not in index:
                return False
            pos = binary(j, index[char])
            if pos == len(index[char]):
                return False
            j = index[char][pos] + 1
        return True