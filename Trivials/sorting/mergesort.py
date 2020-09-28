def mergesort(unordered_list):
    if len(unordered_list) <= 1:
        return unordered_list
    idxm = len(unordered_list) // 2
    left_list = unordered_list[:idxm]
    right_list = unordered_list[idxm:]
    left_list = mergesort(left_list)
    right_list = mergesort(right_list)
    return list(merge(left_list, right_list))


def merge(left_list, right_list):
    res = []
    while len(left_list) != 0 and len(right_list) != 0:
        if left_list[0] < right_list[0]:
            res.append(left_list[0])
            left_list.remove(left_list[0])
        else:
            res.append(right_list[0])
            right_list.remove(right_list[0])
    if len(left_list) == 0:
        res += right_list
    else:
        res += left_list
    return res


unsorted_list = [64, 34, 25, 12, 22, 11, 90]
print(mergesort(unsorted_list))
