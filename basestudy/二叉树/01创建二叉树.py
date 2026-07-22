from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 创建二叉树 先根节点再左子树右子树
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


# tree=[1,2,3,4,None,5]

# 前序遍历  根左右
class Solution:
    def preorder(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return

            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res
    #中序遍历  左根右
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res

    #后续遍历  左右根
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res