class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_dict = {}
        intersection = []

        for num1 in nums1:
            my_dict[num1] = my_dict.get(num1, 0) + 1

        for num2 in nums2:
            if num2 in my_dict:
                intersection.append(num2)
                my_dict[num2] -= 1
                if my_dict[num2] == 0:
                    del my_dict[num2]
        return intersection