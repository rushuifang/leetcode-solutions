"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

# My recursion
class Solution:
    def getImportance(self, employees: List["Employee"], id: int) -> int:
        emap = {employee.id: employee for employee in employees}

        def dfs(eid):
            res = emap[eid].importance
            for subordinate in emap[eid].subordinates:
                res += dfs(subordinate)
            return res

        return dfs(id)


# My bfs
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees: List["Employee"], id: int) -> int:
        emap = {employee.id: employee for employee in employees}

        queue = []
        visited = set()
        queue.append((id, emap[id].importance))
        res = 0

        while queue:
            eid, value = queue.pop(0)
            res += value
            for child in emap[eid].subordinates:
                if child not in visited:
                    queue.append((child, emap[child].importance))
                    visited.add(child)
        return res