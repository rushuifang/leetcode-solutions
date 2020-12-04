class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        ans = []
        start = 0
        end = 0
        
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                end = i
                if end == len(s) - 1 and end - start >= 2:
                    ans.append([start, end])
            else:
                if end - start >= 2:
                    ans.append([start, end])
                start = i
            
        return ans

# Two pointers!
class Solution(object):
    def largeGroupPositions(self, S):
        ans = []
        i = 0 # The start of each group
        for j in xrange(len(S)):
            if j == len(S) - 1 or S[j] != S[j+1]:
                # Here, [i, j] represents a group.
                if j-i+1 >= 3:
                    ans.append([i, j])
                i = j+1
        return ans