from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)

# tree=[1,2,3,4,None,5]

# 前序遍历  根左右
def preorder(root:TreeNode)->List[int]:
    res=[]

    def dfs(node):
        if not node:
            return
        res.append(node.val)
        dfs(node.left)
        dfs(node.right)
    dfs(root)
    return res

