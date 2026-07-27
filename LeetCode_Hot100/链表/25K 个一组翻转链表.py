# Definition for singly-linked list.

from typing import Optional,List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0, head)  # 创建虚拟节点，方便后续操作，等价于 dummy=ListNode(0),  dummy.next=head

        pre = dummy  # 记录前驱节点，pre.next指向当前组的第一个节点head

        while True:

            end = pre  # 创建局部变量end，将end指向当前组的最后一个节点head
            for _ in range(k):#循环k次，找到当前组的最后一个节点，如果不满足k个节点，直接返回虚拟节点的下一个节点head
                end = end.next
                if not end:
                    return dummy.next

            next_group = end.next#记录下组的第一个节点，用于连接下组

            start = pre.next#记录当前组的第一个节点，用于连接下组的前驱节点pre
            # start.next=next_group
            cur = start
            pre_node = next_group

            while cur != next_group:
                nxt = cur.next
                cur.next = pre_node
                pre_node = cur
                cur = nxt

            pre.next = pre_node
            start.next = next_group

            pre = start












