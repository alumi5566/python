import sys


def getCount(alist, element):
    leng = len(alist)
    count = 0
    for i in range(leng):
        if alist[i] == element:
            count += 1
    return count


def getMajorEle(alist):
    leng = len(alist)
    print("len = ", leng)
    if leng == 1:
        return alist[0]
    mid = int(leng / 2)
    print(f"mid = ", mid)
    programPause = input("Press the <ENTER> key to continue...")
    lElement = getMajorEle(alist[:mid])
    rElement = getMajorEle(alist[mid:])
    if lElement == rElement:
        return lElement
    lCnt = getCount(alist, lElement)
    rCnt = getCount(alist, rElement)
    if lCnt > mid:
        return lElement
    elif rCnt > mid:
        return rElement
    else:
        return -1


alist = [2, 4, 4, 4, 6, 6, 6, 8]
Maj = getMajorEle(alist)
print('Major is ', Maj, '!!!')
