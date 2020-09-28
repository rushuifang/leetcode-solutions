def bsearch(list, val):
    idx0 = 0
    idxn = len(list) - 1

    while idx0 <= idxn:
        idxm = (idx0 + idxn) // 2
        if list[idxm] == val:
            return idxm
        if list[idxm] < val:
            idx0 = idxm + 1
        else:
            idxn = idxm - 1

    if idx0 > idxn:
        return None


list = [2, 7, 19, 34, 53, 72]
print(bsearch(list, 72))
print(bsearch(list, 11))
