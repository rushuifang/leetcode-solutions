class Solution:
    def findMaximizedCapital(
        self, k: int, W: int, Profits: List[int], Capital: List[int]
    ) -> int:
        L = len(Profits)
        money = []
        for i in range(L):
            money.append((Profits[i], Capital[i]))
        money.sort(key=lambda x: x[1])
        index = 0
        profitsq = []
        while k > 0:
            for i in range(index, L):
                if W >= money[i][1]:
                    heapq.heappush(profitsq, (-money[i][0]))
                    index = i + 1
                else:
                    break
            if profitsq:
                W += -heapq.heappop(profitsq)
            else:
                break
            k -= 1
        return W
