
import sys


def GetCount(alist,element):
	leng = len(alist)
	count = 0
	for i in range(leng):
		if alist[i] == element:
			count+=1
	return count

def GetMajorEle(alist):
	leng = len(alist)
	print "len = ",leng
	if leng == 1:
		return alist[0]
	mid = leng/2
	print "mid = ",mid
	#wait = input("PRESS ENTER TO CONTINUE.")
	programPause = raw_input("Press the <ENTER> key to continue...")
	Lelement = GetMajorEle(alist[:mid])
	Relement = GetMajorEle(alist[mid:])
	if Lelement == Relement:
		return Lelement
	Lcnt = GetCount(alist,Lelement)
	Rcnt = GetCount(alist,Relement)
	if Lcnt > mid:
		return Lelement
	elif Rcnt > mid:
		return Relement
	else:
		return -1

alist = [2,4,4,4,6,6,6,8]
Maj = GetMajorEle(alist)
print 'Major is ',Maj,'!!!'
