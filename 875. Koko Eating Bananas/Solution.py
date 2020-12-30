class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        piles.sort()
        
        def helper(k):
            hours = 0
            for pile in piles:
                if pile % k == 0:
                    hours += pile//k
                else:
                    hours += pile//k + 1
            if hours <= H:
                return True
            
        left = 1 
        right = piles[-1]
        while left < right:
            mid = (left + right) // 2
            if helper(mid):
                right = mid
            else:
                left = mid + 1
        return left
            