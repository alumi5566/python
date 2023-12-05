class DualNode(object):
    def __init__(self, count, keys = []):
        self.count = count
        self.keys = set(keys)
        self.left = None
        self.right = None

class AllOne(object):
    def __init__(self):
        self.maxNode = DualNode(-1, [])
        self.minNode = DualNode(-1, [])
        self.maxNode.right = self.minNode
        self.minNode.left = self.maxNode
        self.record_key = {} # {"str", Node}
        self.record_cnt = {} # {1, set("str", ""str2"", ...)}

    def printChain(self):
        curPos = self.maxNode
        i = 0
        while curPos != None:
            print("\t", curPos)
            print("\t", i,"th node, val: ", curPos.count, " set: ", list(curPos.keys))
            print("\tleft: ", curPos.left, "right ", curPos.right)
            i += 1
            curPos = curPos.right
        print("record_key", self.record_key)
        print("record_cnt", self.record_cnt)
        return

    def inc(self, key):
        """
        :type key: str
        :rtype: None
        """
        print("inc: ", key)
        if self.maxNode.right == self.minNode and self.minNode.left == self.maxNode:
            # print("first time inc")
            node = DualNode(1, [key])
            node.left = self.maxNode
            self.maxNode.right = node
            node.right = self.minNode
            self.minNode.left = node
            self.record_key[key] = node
            self.record_cnt[1] = set([key])
            return

        # need to add new record (key: 1)
        if key not in self.record_key.keys():
            print("key not in self.record_key.keys")
            # see if we have other 1
            if 1 in self.record_cnt.keys():
                print("1 in self.record_cnt.keys()")
                oneKey = list(self.record_cnt[1])[0]
                oneNode = self.record_key[oneKey]
                oneNode.keys.add(key)
                self.record_key[key] = oneNode
                self.record_cnt[1].add(key)
            # new 1
            else:
                # print("1 not in self.record_cnt.keys()")
                # print("curSmallest: ", self.minNode.left.count)
                curSmallest = self.minNode.left
                node = DualNode(1, [key])
                node.left = curSmallest
                node.right = self.minNode
                curSmallest.right = node
                self.minNode.left = node
                self.record_key[key] = node
                self.record_cnt[1] = set([key])
        # need to update existing record
        else:
            # print("key in self.record_key.keys")
            # print("self.record_key ", self.record_key)
            # print("self.record_cnt ", self.record_cnt)
            curNode = self.record_key[key]
            curCnt = curNode.count
            listOfKeys = self.record_cnt[curCnt]
            # print("curNode: ", curNode)
            # see if we have left node
            if curCnt+1 in self.record_cnt.keys():
                leftKey = list(self.record_cnt[curCnt+1])[0]
                leftNode = self.record_key[leftKey]
                leftNode.keys.add(key)
                self.record_key[key] = leftNode
                self.record_cnt[curCnt+1].add(key)
            elif curNode.left != self.maxNode:
            # if curNode.left != self.maxNode:
                left = curNode.left
                node = DualNode(curCnt+1, [key])
                node.right = left.right
                left.right.left = node
                left.right = node
                node.left = left
                self.record_key[key] = node
                self.record_cnt[curCnt+1] = set([key])
            # add new left node
            else:
                curBiggest = self.maxNode.right
                node = DualNode(curCnt+1, [key])
                curBiggest.left = node
                node.right = curBiggest
                node.left = self.maxNode
                self.maxNode.right = node
                self.record_key[key] = node
                self.record_cnt[curCnt+1] = set([key])

            # print("removing...")
            # print("self.record_key ", self.record_key)
            # print("self.record_cnt ", self.record_cnt)
            # print("curNode: ", curNode)
            # keep the node
            if len(listOfKeys) > 1:
                curNode.keys.remove(key)
                s = self.record_cnt[curCnt]
                s.remove(key)
                self.record_cnt[curCnt] = s
            # remove node
            else:
                curNode.left.right = curNode.right
                curNode.right.left = curNode.left
                self.record_cnt.pop(curCnt)
            # print("done!!!!")
            # print("self.record_key ", self.record_key)
            # print("self.record_cnt ", self.record_cnt)
            # print("curNode: ", curNode)

    def dec(self, key):
        """
        :type key: str
        :rtype: None
        """
        print("dec: ", key)
        curNode = self.record_key[key]
        curCnt = curNode.count
        listOfKeys = self.record_cnt[curCnt]
        # add a record in curCnt-1
        if curCnt-1 != 0:
            if curCnt-1 in self.record_cnt.keys():
                rightKey = list(self.record_cnt[curCnt-1])[0]
                rightNode = self.record_key[rightKey]
                rightNode.keys.add(key)
                self.record_key[key] = rightNode
                self.record_cnt[curCnt-1].add(key)
            elif curNode.right != self.minNode:
                right = curNode.right
                node = DualNode(curCnt-1, [key])
                node.left = right.left
                node.right = right
                right.left.right = node
                right.left = node
                self.record_key[key] = node
                self.record_cnt[curCnt-1] = set([key])
            else:
                curSmallest = self.minNode.left
                node = DualNode(curCnt-1, [key])
                curSmallest.right = node
                node.right = curSmallest
                node.right = self.minNode
                self.minNode.left = node
                self.record_key[key] = node
                self.record_cnt[curCnt-1] = set([key])
        print("removing...")
        # print("self.record_key ", self.record_key)
        # print("self.record_cnt ", self.record_cnt)
        # print("curNode: ", curNode)
        # keep the node
        if curCnt-1 != 0:
            if len(listOfKeys) > 1:
                curNode.keys.remove(key)
                s = self.record_cnt[curCnt]
                s.remove(key)
                self.record_cnt[curCnt] = s
            # remove node
            else:
                curNode.left.right = curNode.right
                curNode.right.left = curNode.left
                self.record_cnt.pop(curCnt)
            # if self.record_key[key].count == 0:
            # self.record_key.pop(key)
        else:
            if len(listOfKeys) > 1:
                curNode.keys.remove(key)
                s = self.record_cnt[curCnt]
                s.remove(key)
                self.record_cnt[curCnt] = s
            # remove node
            else:
                curNode.left.right = curNode.right
                curNode.right.left = curNode.left
                self.record_cnt.pop(curCnt)
                self.record_key.pop(key)
        # print("done!!!!")
        # print("self.record_key ", self.record_key)
        # print("self.record_cnt ", self.record_cnt)
        # print("curNode: ", curNode)
        # return


    def getMaxKey(self):
        """
        :rtype: str
        """
        cnt = self.maxNode.right.count
        return list(self.record_cnt[cnt])[0]
        # return self.maxNode.right.count

    def getMinKey(self):
        """
        :rtype: str
        """
        cnt = self.minNode.left.count
        return list(self.record_cnt[cnt])[0]
        # return self.minNode.left.count

# TC 1
# allOne = AllOne()
# allOne.inc("hello")
# allOne.inc("hello")
# print allOne.getMaxKey()
# print allOne.getMinKey()
# allOne.inc("leet")
# print allOne.getMaxKey()
# print allOne.getMinKey()
# TC 2
# allOne.inc("a")
# allOne.inc("a")
# allOne.inc("a")
# allOne.inc("a")
# allOne.inc("a")
# allOne.printChain()
# allOne.inc("b")
# allOne.printChain()
# allOne.inc("b") # ->
# allOne.inc("b")
# allOne.inc("b")
# allOne.inc("b")
# allOne.inc("c")
# allOne.inc("c")
# allOne.inc("c")
# allOne.inc("c")
# allOne.inc("d")
# allOne.inc("d")
# allOne.inc("d")
# allOne.inc("d")
# allOne.inc("e")
# allOne.inc("e")
# allOne.inc("e")
# allOne.inc("f")
# allOne.inc("g")
# allOne.printChain()
# print(allOne.getMaxKey())
# print(allOne.getMinKey())
# allOne.dec("a")
# allOne.dec("c")
# allOne.dec("e")
# allOne.dec("g")
# allOne.dec("f")
# allOne.printChain()

# TC 4
# alltwo = AllOne()
# file1 = open('input1.txt', 'r')
# file2 = open('input2.txt', 'r')
# Lines1 = file1.readlines()
# Lines2 = file2.readlines()
#
# count = 0
# # Strips the newline character
# for i in range(len(Lines1)):
#     count += 1
#     # print("Line{}: {}".format(count, Lines1[i].strip()))
#     # print("Line{}: {}".format(count, Lines2[i].strip()))
#     print("Line{}: {} {}".format(count, Lines1[i].strip(), Lines2[i].strip(), ))
#     if Lines1[i].strip() == "inc":
#         alltwo.inc(Lines2[i].strip())
#     elif Lines1[i].strip() == "dec":
#         alltwo.dec(Lines2[i].strip())
#     elif Lines1[i].strip() == "getMaxKey":
#         alltwo.getMaxKey()
#     elif Lines1[i].strip() == "getMinKey":
#         alltwo.getMaxKey()
#     if count > 10000:
#         alltwo.printChain()

# TC 5
# ["AllOne","inc","inc","inc","inc","getMaxKey","inc","inc","inc","dec","inc","inc","inc","getMaxKey"]
# [[],["hello"],["goodbye"],["hello"],["hello"],[],["leet"],["code"],["leet"],["hello"],["leet"],["code"],["code"],[]]
# allOne = AllOne()
# allOne.inc("hello")
# allOne.inc("goodbye")
# allOne.inc("hello")
# allOne.inc("hello")
# print(allOne.getMaxKey())
# # allOne.printChain()
# allOne.inc("leet")
# allOne.inc("code")
# allOne.inc("leet")
# allOne.printChain()
# allOne.dec("hello")
# allOne.printChain()
# allOne.inc("leet")
# allOne.printChain()
# allOne.inc("code")
# allOne.inc("code")
# print(allOne.getMaxKey())

# TC 6
# ["AllOne","inc","inc","inc","inc","inc","inc","dec", "dec","getMinKey","dec","getMaxKey","getMinKey"]
# [[],["a"],["b"],["b"],["c"],["c"],["c"],["b"],["b"],[],["a"],[],[]]
allOne = AllOne()
allOne.inc("a")
allOne.inc("b")
allOne.inc("b")
allOne.inc("c")
allOne.inc("c")
allOne.inc("c")
allOne.printChain()
allOne.dec("b")
allOne.printChain()
allOne.dec("b")
allOne.printChain()
print(allOne.getMinKey())
# allOne.printChain()
allOne.dec("a")
print(allOne.getMaxKey())
print(allOne.getMinKey())

