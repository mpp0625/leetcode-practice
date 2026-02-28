from typing import Optional

from utils.linked_list import ListNode, createLinkedList, reverseLinkedList


head, _ = createLinkedList([1,2,3,4,5])
print(reverseLinkedList(head))


"""
遍历链表，当前节点的 next 改为指向前一个节点，然后更新前一个节点为当前节点，当前节点为下一个节点
"""