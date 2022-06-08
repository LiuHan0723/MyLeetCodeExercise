class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
t1=TreeNode(val=3)
t4=TreeNode(val=5,left=t1)
t3=TreeNode(val=2)
t2=TreeNode(val=4,left=t3,right=t4)


import heapq
class Solution(object):
    res = []

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return 0
        self.dfs(root, )
        return Solution.res[k-1]

    def dfs(self, root, ):

        if root:
            self.dfs(root.left)
            Solution.res.append(root.val)
            self.dfs(root.right)

if __name__ == '__main__':
    sol=Solution()
    print(sol.kthSmallest(t2,1))