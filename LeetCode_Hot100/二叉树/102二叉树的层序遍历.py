#102. 二叉树的层序遍历
'''
提示:给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]

示例 2：
输入：root = [1]
输出：[[1]]

示例 3：
输入：root = []
输出：[]

提示：
树中节点数目在范围 [0, 2000] 内
-1000 <= Node.val <= 1000
'''


# Definition for a binary tree node.

from collections import deque
from typing import List, Optional
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        queue=deque([root])#队列存储待处理的二叉树节点
        result=[]#存储最终的结果，每个元素是一个列表，表示一层的节点值

        while queue:#当队列不为空时，说明还有节点需要处理，queue在变化
            total_lev=len(queue)#当前层的节点数量 1，2，4随着队列节点的数量变化
            cur_lev=[]#临时存储当前层的节点值

            for _ in range(total_lev):#遍历当前层的所有节点

                node =queue.popleft()#从队列中取出最左侧的节点
                cur_lev.append(node.val)#将节点值加入临时列表

                if node.left:
                    queue.append(node.left)#将左子树节点加入队列，等待后续处理

                if node.right:
                    queue.append(node.right)#将右子树节点加入队列，等待后续处理

            result.append(cur_lev)#将当前层的节点值加入结果列表

        return result   # 






