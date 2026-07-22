# 543.二叉树的直径
# 给你一棵二叉树的根节点，返回该树的直径 。
# 二叉树的直径是指树中任意两个节点之间最长路径的长度 。这条路径可能经过也可能不经过根节点root 。
# 两节点之间路径的长度由它们之间边数表示。
#
# 示例1：
# 输入：root = [1, 2, 3, 4, 5]
# 输出：3
# 解释：3 ，取路径[4, 2, 1, 3]
# 或[5, 2, 1, 3]
# 的长度。
#
# 示例2：
# 输入：root = [1, 2]
# 输出：1
#
# 提示：

# 树中节点数目在范围[1, 104]内
# -100 <= Node.val <= 100

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        if not root:
            return 0
        def dfs(node):

            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)

            self.max_diameter = max(left_depth+right_depth,self.max_diameter)

            return max(left_depth,right_depth)+1

        dfs(root)
        return self.max_diameter
