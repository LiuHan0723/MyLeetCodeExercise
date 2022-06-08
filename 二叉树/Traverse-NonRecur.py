


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

t2=TreeNode(2)
t3=TreeNode(3)
t1=TreeNode(1,t2,t3)

# def traverse(Node):
#
#     if Node:
#
#         traverse(Node.left)
#         print(Node.val)
#         traverse(Node.right)

class Command:

    def __init__(self,s,node):
        self.s=s
        self.node=node

def preTraverse(root):

    stack=[]
    res=[]

    cmd=Command("run",root)
    stack.append(cmd)

    while stack:
        cmd_state=stack.pop()

        if  cmd_state.s=="print":
            res.append(cmd_state.node.val)
        else:

            if cmd_state.node.right:
                stack.append(Command("run",cmd_state.node.right))

            if cmd_state.node.left:
                stack.append(Command("run",cmd_state.node.left))
            stack.append(Command("print", cmd_state.node))

    return res
if __name__ == '__main__':
    print(preTraverse(t1))