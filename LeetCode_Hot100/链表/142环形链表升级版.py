# 142.环形链表II
#
# 给定一个链表的头节点
# head ，返回链表开始入环的第一个节点。 如果链表无环，则返回
# null。
#
# 如果链表中有某个节点，可以通过连续跟踪next指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数
# pos来表示链表尾连接到链表中的位置（索引从0开始）。如果pos是 - 1，则在该链表中没有环。注意：pos
# 不作为参数进行传递，仅仅是为了标识链表的实际情况。不允许修改链表。
#
# 示例1：
# 输入：head = [3, 2, 0, -4], pos = 1
# 输出：返回索引为1的链表节点
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
# 示例2：
# 输入：head = [1, 2], pos = 0
# 输出：返回索引为0的链表节点
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
# 示例3：
# 输入：head = [1], pos = -1
# 输出：返回null
# 解释：链表中没有环。


# Definition for singly-linked list.
from typing import Optional

from sympy.codegen.ast import none


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 方法1：哈希表
        # cur=head
        # dict=set()
        # while cur:
        #     if cur in dict:
        #         return cur
        #     dict.add(cur)
        #     cur=cur.next
        # return None

        # 方法2：快慢指针，先找环，再找环入口
        # 1. 第一阶段：快慢指针找相遇点
        slow = head
        fast = head

        while fast and fast.next:  # 防止 fast 掉出链表（无环情况）
            slow = slow.next
            fast = fast.next.next
            if slow == fast:      # 找到相遇点了！
                # 2. 第二阶段：一个从head走，一个从相遇点走
                ptr1 = head
                ptr2 = slow        # 或者 fast（因为此时它俩在一起）
                while ptr1 != ptr2:
                    ptr1 = ptr1.next
                    ptr2 = ptr2.next
                return ptr1       # 这就是环入口

        # 如果 while 结束（fast 到了 None），说明无环
        return None

