from typing import Optional

from utils.linked_list import ListNode, createLinkedList


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head

    while curr:
        next_node = curr.next
        
        curr.next = prev
        prev = curr

        curr = next_node

    return prev


head, _ = createLinkedList([1,2,3,4,5])
print(reverseList(head))


"""
遍历链表，当前节点的 next 改为指向前一个节点，然后更新前一个节点为当前节点，当前节点为下一个节点
"""