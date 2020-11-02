class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1map, s2map = [0]*26, [0]*26
        
        for i in range(len(s1)):
            s1map[ord(s1[i]) - ord("a")] += 1
            s2map[ord(s2[i]) - ord("a")] += 1
        
        if s1map == s2map:
            return True
        for j in range(len(s2) - len(s1)):
            s2map[ord(s2[len(s1) + j]) - ord("a")] += 1
            s2map[ord(s2[j]) - ord("a")] -= 1
            if s1map == s2map:
                return True
        return False