class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        heap, ans = [], []
        for start, end in intervals + [newInterval]:
            heapq.heappush(heap, (start, -1))
            heapq.heappush(heap, (end, 1))
        
        curr = 0
        start = None
        while heap:
            num, flag = heapq.heappop(heap)
            if start == None: start = num 
            curr += flag
            
            if curr == 0:
                ans.append([start ,num])
                start = None
        return ans