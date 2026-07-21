#19. 删除链表的倒数第 N 个结点
# 给你一个链表的头结点 head 和一个整数 n ，
# 请你返回删除链表的倒数第 n 个结点后的链表头结点。
#示例 1：
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]

# 示例 2：
# 输入：head = [1], n = 1
# 输出：[]
# 示例 3：
# 输入：head = [1,2], n = 1
# 输出：[1]
#
# 提示：链表中结点的数目为 sz
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz



# Definition for singly-linked list.

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy = head.next
        low = fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            low = low.next

        low.next = low.next.next
        return dummy.next

