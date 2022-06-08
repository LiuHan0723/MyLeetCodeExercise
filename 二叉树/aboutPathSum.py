class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

t1=TreeNode(5)
t2=TreeNode(val=2,right=t1)
t3=TreeNode(val=3)

root=TreeNode(val=1,left=t2,right=t3)
def binaryTreePaths(root):

    res=[]
    if not root:
        return res

    if root.left == None and root.right == None:
        res.append([root.val])
        return res

    left = binaryTreePaths(root.left)
    right = binaryTreePaths(root.right)

    for i in left:
        if not i:

            res.append([root.val])
        else:
            i.insert(0, root.val)
            res.append(i)

    for j in right:

        if not j:
            res.append([root.val])
        else:
            j.insert(0, root.val)
            res.append(j)

    return res

if __name__ == '__main__':
    print(binaryTreePaths(root))