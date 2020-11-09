class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        ans, idx, width = 0, 0, 0
        inventory.sort(reverse=True)
        inventory.append(0)
        
        while orders > 0:
            width += 1
            sell = min(orders, width*(inventory[idx] - inventory[idx+1]))
            whole, remainder = divmod(sell, width)
            ans += width*(inventory[idx] + inventory[idx] - whole + 1)*whole//2 + remainder*(inventory[idx] - whole)
            orders -= sell
            idx += 1
            
        return ans%(10**9+7)