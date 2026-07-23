# 104. 二叉树的最大深度
#给定一个二叉树 root ，返回其最大深度。
#
# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
#
# 示例 1： 输入：root = [3,9,20,null,null,15,7]
# 输出：3

# 示例 2：
# 输入：root = [1,null,2]
# 输出：2
#
# 提示：
# 树中节点的数量在 [0, 104] 区间内。
# -100 <= Node.val <= 100

# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            left_hight = self.maxDepth(root.left)
            right_hight = self.maxDepth(root.right)
            print(left_hight, right_hight)
            return max(left_hight, right_hight) + 1
            # return max(self.maxDepth(root.left),self.maxDepth(root.right))+1
            # print(left_hight, right_hight)


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(5)
sol = Solution()
sol.maxDepth(root)
print(sol.maxDepth(root))
