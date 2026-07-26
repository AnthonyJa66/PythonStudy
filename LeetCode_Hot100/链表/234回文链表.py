# 234.回文链表
# 给你一个单链表的头节点head ，请你判断该链表是否为回文链表。如果是，返回true ；否则，返回false 。
#
# 示例1：
# 输入：head = [1, 2, 2, 1]
# 输出：true

# 示例2：
# 输入：head = [1, 2]
# 输出：false

# 提示：
# 链表中节点数目在范围[1, 105]
# 内
# 0 <= Node.val <= 9

# 进阶：你能否用O(n)时间复杂度和O(1)空间复杂度解决此题？


# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur=head
        nxt=head.next
        list1=[]
        while cur:
            list1.append(cur.val)
            cur=cur.next
        return list1==list1[::-1]#判断是否为回文列表，也就是正序等于倒序


