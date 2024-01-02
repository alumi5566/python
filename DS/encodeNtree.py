
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def encode(root):
    """Encodes an n-ary tree to a binary tree.
    :type root: Node
    :rtype: TreeNode
    """
    # print(type(root.children))
    def helper(root):
        # print("root.val: ", root.val)
        # print("root.val child len: ", len(root.children))
        if root == None:
            return None
        if root.children == [] or root.children == None:
            return TreeNode(root.val)
        if len(root.children) <= 1:
            ret = TreeNode(root.val)
            ret.left = helper(root.children[0])
            return ret
        else:
            ret = TreeNode(root.val)
            ret.left = helper(root.children[0])
            head = helper(root.children[1])
            tmp = head
            # print("here")
            # print("root.val child len: ", len(root.children))
            for i in range(2, len(root.children)):
                tmp.right = helper(root.children[i])
                tmp = tmp.right
            ret.left.right = head
            return ret
    res = helper(root)
    print("res=", res)
    return res

def decode(data):
    """Decodes your binary tree to an n-ary tree.
    :type data: TreeNode
    :rtype: Node
    """
    # node5 = Node(5)
    # node6 = Node(6)
    # node3 = Node(3, [node5, node6])

    # node2 = Node(2)
    # node4 = Node(4)
    # node1 = Node(1, [node3, node2, node4])
    # print("node: ", node1)
    # return node1
    def helper(root):
        if root == None:
            return None
        print(">root=", root.val)
        child = []
        ret = Node(root.val)
        if root.right != None:
            head = root.right
            while head != None:
                child.append(helper(head)[0])
                head = head.right
        if root.left != None:
            lnode, childs = helper(root.left)
            ret.children = childs
            ret.left = lnode
        print(">ret=", ret.val, "childSize=", len(child))
        return (ret, child)

    return helper(data)[0]

def dfs(root):
    def output(node):
        if node == None:
            return "None"
        else:
            return str(node.val)
    if root == None:
        return
    print("root: ", root.val, " l: ", output(root.left), " r: ", output(root.right))
    dfs(root.left)
    dfs(root.right)

def dfsN(root):
    def output(node):
        if node == None:
            return "None"
        else:
            return str(node.val)
    if root == None:
        return
    print("root: ", root.val)
    if root.children != [] and root.children is not None:
        for c in root.children:
            print("\tch: ", c.val)
    if root.children != [] and root.children is not None:
        for c in root.children:
            dfsN(c)


node5 = Node(5)
node6 = Node(6)
node3 = Node(3, [node5, node6])

node2 = Node(2)
node4 = Node(4)
node1 = Node(1, [node3, node2, node4])

print("N1")
N1 = encode(node1)
dfs(N1)

print("N2")
N2 = decode(N1)
dfsN(N2)
# print("N2")
# dfsN(node1)