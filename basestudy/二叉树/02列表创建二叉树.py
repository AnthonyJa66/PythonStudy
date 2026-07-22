from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    # 1. 防御性编程：如果列表为空，直接返回空树
    if not values:
        return None

    # 2. 创建根节点，并放入队列（队列里存放的是“等待领取孩子”的节点）
    root = TreeNode(values[0])
    queue = deque([root])

    # 3. 指针 i 用来指向列表中的下一个待处理元素（从第1个元素开始，因为第0个是根）
    i = 1

    # 只要列表里还有元素没处理，并且队列里还有“等待领孩子的父节点”
    while i < len(values):
        # 从队列中弹出当前需要“领孩子”的父节点
        current_node = queue.popleft()

        # --- 处理左孩子 (列表当前位置的值) ---
        # 如果当前索引 i 没越界
        if i < len(values):
            val = values[i]
            # 如果值不是 None，说明这个左孩子存在，创建它并挂到父节点左边
            if val is not None:
                current_node.left = TreeNode(val)
                # 把这个新创建的孩子加入队列，因为它以后也要“领自己的孩子”
                queue.append(current_node.left)
            # 如果 val 是 None，什么都不用做，left 默认就是 None
            i += 1  # 指针后移，处理下一个列表元素

        # --- 处理右孩子 (列表当前位置的值) ---
        if i < len(values):
            val = values[i]
            if val is not None:
                current_node.right = TreeNode(val)
                queue.append(current_node.right)
            i += 1

    return root

# 测试我们刚才建的树：[1,2,3,None,None,4,5]
# 结构是：
#     1
#    / \
#   2   3
#      / \
#     4   5
# 注意：2的左右孩子都是None，所以后面没有挂任何东西给2。

tree=[1,2,3,4,None,5]
root=build_tree_from_list(tree)
