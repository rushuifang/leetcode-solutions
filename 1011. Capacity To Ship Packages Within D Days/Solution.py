class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def helper(cap):
            days = 0
            stack = 0
            weights_copy = weights[:]
            while weights_copy:
                weight = weights_copy.pop(0)
                if stack + weight > cap:
                    days += 1
                    stack = weight
                elif stack + weight == cap:
                    days += 1
                    stack = 0
                else:
                    stack += weight
            if stack > 0:
                days += 1
            return days <= D
        
 
        low = max(weights)
        high = sum(weights)
        while low < high:
            mid = (low + high) // 2
            if helper(mid):
                high = mid
            else:
                low = mid + 1
        return high

# Better helper function
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def helper(cap):
            i = 0
            for _ in range(D):
                cap_day = cap
                while (cap_day - weights[i]) >= 0:
                    cap_day -= weights[i]
                    i += 1                    
                    if i == len(weights):
                        return True
            return False
                
 
        low = max(weights)
        high = sum(weights)
        while low < high:
            mid = (low + high) // 2
            if helper(mid):
                high = mid
            else:
                low = mid + 1
        return high