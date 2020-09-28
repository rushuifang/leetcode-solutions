def insertionsort(uoList):
    for i in range(1, len(uoList)):
        j = i - 1
        nxt = uoList[i]
        while (uoList[j] > next) and (j >= 0):
            uoList[j + 1] = uoList[j]
            j -= 1
        uoList[j + 1] = next


uoList = [19, 2, 31, 45, 30, 11, 121, 27]
insertionsort(uoList)
print(uoList)