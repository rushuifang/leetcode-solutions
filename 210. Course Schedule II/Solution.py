class Solution:
    WHITE = 1
    GREY = 2
    BLACK = 3
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        POSSIBLE = True
        adj_list = collections.defaultdict(list)
        for el in prerequisites:
            adj_list[el[1]].append(el[0])
        color = {k:Solution.WHITE for k in range(numCourses)}
        stack = []
        
        def dfs(node):
            nonlocal POSSIBLE
            if not POSSIBLE:
                return
            color[node] = Solution.GREY
            for neighbor in adj_list[node]:
                if color[neighbor] == Solution.GREY:
                    POSSIBLE = False
                elif color[neighbor] == Solution.WHITE:
                    dfs(neighbor)
            color[node] = Solution.BLACK
            stack.append(node)
            
        for i in range(numCourses):
            if color[i] == Solution.WHITE:
                dfs(i)
        if POSSIBLE:
            return stack[::-1]
        else:
            return []
            