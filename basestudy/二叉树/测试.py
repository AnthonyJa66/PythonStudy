from collections import deque
from idlelib.tree import TreeNode
from typing import List,Optional

class Node:
    def __init__(self,val=0,left=None,Right=None):
        self.val=val
        self.left=left
        self.right=Right

#def buildTreebyList(self,values:List[Optional[int]])->Optional[TreeNode]:

#ListA:List[Optional[int]]中的Optional的作用：参数 ListA 是一个列表，这个列表里的每一个元素，要么是int（整数），要么是 None。
def buildtreebylist(ListA:List[Optional[int]])->Optional[TreeNode]:
    #Optional[TreeNode]中的Optional的作用：这个函数返回的结果，要么是一个TreeNode对象，要么是 None

    if not ListA:
        return None
    root=TreeNode(ListA[0])
    queue=deque([root])#用来存储待处理的节点
    i=1
    while i<len(ListA) and queue:

        node=queue.popleft()

        if i<len(ListA):
            if len(ListA) is not None:
                node.left=TreeNode(ListA[i])#创建左子树节点
                queue.append(node.left)#添加左子树节点之后，将节点加入队列，等待后续处理
            i+=1

        if i<len(ListA):
            if len(ListA) is not None:
                node.right=TreeNode(ListA[i])#创建右子树节点
                queue.append(node.right)#添加右子树节点之后，将节点加入队列，等待后续处理
            i+=1
    return root
