from typing import Optional

class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA==None or headB==None:
            return None

        #双指针:curA,curB分别指向链表A和B的头节点,如果curA,curB相交,则curA==curB
        curA = headA
        curB = headB
        while curA != curB:
            curA = curA.next if curA else headB
            '''
            if curA is not None:  # 如果 curA 手里还拿着节点
                curA = curA.next  # 就向前走一步（指向下一个节点）
            else:  # 如果 curA 已经变成 None（走到头了）
                curA = headB  # 就瞬间跳转到链表B的头部
                '''
            curB = curB.next if curB else headA

        return curA




"""
        # 步骤1：创建一个空的集合（Set），用来存放节点
        visited=set()

        # 步骤2：遍历链表A，把每一个节点都丢进集合里
        curA=headA
        while curA:
            visited.add(curA)
            curA=curA.next

        # 步骤3：遍历链表B，检查当前节点是否在集合里
        curB=headB
        while curB:

            # 如果当前节点已经在集合里，说明这就是相交的第一个节点
            if curB in visited:
                return curB
            curB=curB.next
        return None
        """

