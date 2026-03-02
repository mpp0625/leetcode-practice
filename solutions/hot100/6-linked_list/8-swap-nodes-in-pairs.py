from typing import Optional

from utils.linked_list import ListNode, createLinkedList, transformToArray


def swapPairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head
    
    dummy = ListNode(-1, head)
    curr = dummy

    while curr.next and curr.next.next:
        prevNode = curr.next
        nextNode = curr.next.next

        curr.next = nextNode

        prevNode.next = nextNode.next
        nextNode.next = prevNode

        curr = prevNode

    return dummy.next


head, _ = createLinkedList([1,2,3,4,5])
print(transformToArray(swapPairs(head)))