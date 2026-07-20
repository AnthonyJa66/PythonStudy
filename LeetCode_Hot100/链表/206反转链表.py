# Definition for singly-linked list.
from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # 前一个节点，初始为空
        cur = head  # 当前节点，从头开始

        while cur:  # 只要当前节点存在
            # 步骤1：先存好后面的路（救命稻草）
            nxt = cur.next

            # 步骤2：反转箭头！让当前节点指向前一个
            cur.next = prev

            # 步骤3：两根手指同时向前移动
            prev = cur  # 前一个来到当前位置
            cur = nxt  # 当前位置去到刚才保存的下一个位置

        # 循环结束，prev 就是反转后的新头节点
        return prev
