def shellsort(uoList):
    gap = len(uoList) // 2
    while gap > 0:
        for i in range(gap, len(uoList)):
            temp = uoList[i]
            j = i

            while (j >= gap) and uoList[j - gap] > temp:
                uoList[j] = uoList[j - gap]
                j = j - gap
            uoList[j] = temp
        gap = gap // 2


l = [19, 2, 31, 45, 30, 11, 121, 27]
shellsort(l)
print(l)