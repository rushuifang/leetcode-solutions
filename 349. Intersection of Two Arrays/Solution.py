class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1 = list(set(nums1))
        l2 = list(set(nums2))
        res = []
        for el in l1:
            if el in l2:
                res.append(el)
        return res


# solution 2


class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)