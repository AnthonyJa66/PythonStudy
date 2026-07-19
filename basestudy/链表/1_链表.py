

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# node1=ListNode(1)
# node2=ListNode(2)
# node3=ListNode(3)
# node1.next=node2
# node2.next=node3
#
#
#
# node4=ListNode(4)
# node5=ListNode(5)
# node6=ListNode(6)
# node3.next=node4
# node4.next=node5
# node5.next=node6
#
# cur=node1
# while cur:
#     print(cur.val)
#     cur=cur.next

def add_at_tail(head,val):
    new_node=ListNode(val)#将值传给新节点

    # 如果链表是空的，新节点就是头节点
    if head is None:
        return new_node
    cur=head
    while cur.next is not None:
        cur=cur.next

    cur.next=new_node
    return head

head=ListNode(7)
# head.next=ListNode(8)
# head.next.next=ListNode(9)
h=add_at_tail(ListNode(11),10)
print(h,h.val,h.next)
# cur=head
# while cur:
#     print(cur.val)
#     cur=cur.next

def reverseList(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next   # 保存下一个
        cur.next = prev  # 反转指向
        prev = cur       # 移动
        cur = nxt
    return prev


#
# class Solution:
#     def removeElements(self,head,val):
#         dummy_head=ListNode(next=head)
#         current=dummy_head
#         while current.next:
#             if current.next.val==val:
#                 current.next=current.next.next
#             else:
#                 current=current.next
#         return dummy_head.next
