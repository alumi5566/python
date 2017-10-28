
import sys

def GetXpair_cross(listA,listB):
	i = 0
	j = 0
	index = i
	cnt = 0
	c = []
	for s in range(len(listA)+len(listB)):
		c.append(-1)
	while i<len(listA) and j<len(listB):
		if listA[i] <= listB[j]:
			c[index] = listA[i]
			i+=1
		else:
			c[index] = listB[j]
			j+=1
			cnt += len(listA)-i
			print cnt
		index += 1
	#end while
	if i == len(listA):
		for s in range(j,len(listB)):
			c[index] = listB[s]
			index += 1
	else:
		for s in range(i,len(listA)):
			c[index] = listA[s]
			index += 1
	for s in range(len(listA)):
		listA[s] = c[s]
	for s in range(len(listB)):
		listB[s] = c[s+len(listA)]
	print "the sorted arrayA", listA
	print "the sorted arrayB", listB
	return cnt

def GetXpair(alist):
	leng = len(alist)
	print "len = ",leng
	if leng == 1:
		return 0
	mid = leng/2
	print "mid = ",mid
	Lpair = GetXpair(alist[:mid])
	Rpair = GetXpair(alist[mid:])
	LRpair = GetXpair_cross(alist[:mid],alist[mid:])
	return Lpair+Rpair+LRpair

def test(aaaalist):
	aaaalist[0] = 0

alist = [4,3,1,2]
#Maj = GetMajorEle(alist)
Xpair = GetXpair(alist)
#print 'Major is ',Maj,'!!!'
#print alist
#test(alist)
#print alist
print "Xpair",Xpair
