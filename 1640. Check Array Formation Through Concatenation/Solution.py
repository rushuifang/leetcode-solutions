class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        test = []
        while arr:
            test.append(arr.pop(0))
            if test in pieces:
                pieces.remove(test)
                test = []
        if test == []:
            return True
        else:
            return False