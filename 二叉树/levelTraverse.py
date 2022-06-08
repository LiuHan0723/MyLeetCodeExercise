
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


t7=TreeNode(7)
t6=TreeNode(6)
t5=TreeNode(5)
t4=TreeNode(4)
t2 = TreeNode(2,t4,t5)
t3 = TreeNode(3,t6,t7)
t1 = TreeNode(1, t2, t3)


def levelTraverse(tree):

    q=[(tree,0)]
    res=[]

    while q:
        bottom=q[0]
        q.remove(bottom)
        if bottom[1]==len(res):
            res.append([])
        res[bottom[1]].append(bottom[0].val)
        if bottom[0].left:
            q.append((bottom[0].left,bottom[1]+1))
        if bottom[0].right:
            q.append((bottom[0].right,bottom[1]+1))
    return res
def heapTest():

    pass
if __name__ == '__main__':
    print(levelTraverse(t1))