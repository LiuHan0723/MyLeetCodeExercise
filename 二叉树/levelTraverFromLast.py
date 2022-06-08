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
def levelOrderBottom(root):
    if not root:
        return []

    q = [(root, 0)]
    stack = []

    while q:

        node = q[0][0]
        level = q[0][1]
        stack.append((node, level))
        q.remove(q[0])
        if node.right:
            q.append((node.right, level+1))

        if node.left:
            q.append((node.left, level+1))

    node_level = stack.pop()
    max_length = node_level[1]
    res = [[] for i in range(max_length+1)]
    res[0].append(node_level[0].val)

    while stack:
        node_level = stack.pop()
        res[max_length - node_level[1]].append(node_level[0].val)

    return res

if __name__ == '__main__':
    levelOrderBottom(t1)