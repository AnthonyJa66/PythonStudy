# 98.验证二叉搜索树
# 给你一个二叉树的根节点root，判断其是否是一个有效的二叉搜索树。有效二叉搜索树定义如下：
# 节点的左子树只包含严格小于当前节点的数。
# 节点的右子树只包含严格大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。

# 示例1：
# 输入：root = [2, 1, 3]
# 输出：true

# 示例 2：
# 输入：root = [5, 1, 4, null, null, 3, 6]
# 输出：false
# 解释：根节点的值是5 ，但是右子节点的值是4 。
#

# 提示：
# 树中节点数目范围在[1, 104]
# 内
# -231 <= Node.val <= 231 - 1

# Definition for a binary tree node.

from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # if root is None:
        #     return True
        # queue = deque([root])
        # while queue:
        #     cur = queue.popleft()
        #     if cur.left:
        #         left = cur.left
        #         if left.val < cur.val:
        #             queue.append(left)
        #         else:
        #             return False
        #     if cur.right:
        #         right = cur.right
        #         if right.val > cur.val:
        #             queue.append(right)
        #         else:
        #             return False
        #
        # return True

        prev=float('-inf')#创建一个负无穷大的变量，用来对比最左子树节点的值+记录上一个节点的值

        def inorder(node):#中序遍历

            nonlocal prev #在函数内部修改外部变量 prev

            if not node:#如果节点为空，直接返回True
                return True

            if not inorder(node.left):#如果左子树不是二叉搜索树，直接返回False
                return False

            if node.val<= prev:#如果当前节点的值小于等于上一个节点的值，直接返回False
                return False

            prev = node.val #将当前节点的值赋值给 prev，用来对比下一次节点的值

            return inorder(node.right)#如果右子树是二叉搜索树，直接返回True

        return inorder(root)#运行中序遍历函数，开始






