class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr) < 3:
            return False
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                if i != len(arr) - 2:
                    continue
                else:
                    return False
            else:
                if i == 0:
                    return False
                else:
                    idx = i
                    break
        for i in range(idx, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                continue
            else:
                return False
        return True