class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backTrack(path, choices):
            if not choices:
                result.append(path[:])
                
            for i in range(len(choices)):
                choice = choices.pop(i)
                path.append(choice)
                backTrack(path, choices)
                path.pop()
                choices.insert(i, choice)
        
        result = []
        backTrack([], nums)
        return result