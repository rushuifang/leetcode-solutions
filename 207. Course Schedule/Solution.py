# My wrong solutions forgetting about some courses needs two or more prerequisites.
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        primaryCourses = [i for i in range(numCourses)]
        for pre in prerequisites:
            if pre[0] in primaryCourses:
                primaryCourses.remove(pre[0])
        queue = primaryCourses

        while queue:
            course = queue.pop(0)
            i = 0
            while i < len(prerequisites):
                if prerequisites[i][1] == course:
                    queue.append(prerequisites[i][0])
                    prerequisites.pop(i)
                else:
                    i += 1
        return len(prerequisites) == 0


# Solution
# inorder describes how many pres a successor needs
# outorder is a dict of pre : successors
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inorder = [0 for _ in range(numCourses)]
        outorder = collections.defaultdict(list)
        for el in prerequisites:
            inorder[el[0]] += 1
            outorder[el[1]].append(el[0])
        queue = [idx for idx, el in enumerate(inorder) if el == 0]

        while queue:
            course = queue.pop(0)
            for successor in outorder[course]:
                inorder[successor] -= 1
                if inorder[successor] == 0:
                    queue.append(successor)

        return sum(inorder) == 0