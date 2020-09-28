def selectionsort(uoList):
    for idx in range(len(uoList)):
        min_idx = idx
        for j in range(idx + 1, len(uoList)):
            if uoList[min_idx] > uoList[j]:
                min_idx = j
        uoList[idx], uoList[min_idx] = uoList[min_idx], uoList[idx]


l = [19, 2, 31, 45, 30, 11, 121, 27]
selectionsort(l)
print(l)
