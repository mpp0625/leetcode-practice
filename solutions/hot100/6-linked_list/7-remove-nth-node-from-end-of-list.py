from typing import Optional

from utils.linked_list import ListNode, createLinkedList, transformToArray


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    def getLength(head: Optional[ListNode]):
        if not head:
            return 0
        
        l = 0
        while head:
            l += 1
            head = head.next

        return l

    dummy = ListNode(0, head)
    curr = dummy

    l = getLength(head)

    for _ in range(1, l - n + 1):
        curr = curr.next

    if curr.next:
        curr.next = curr.next.next

    return dummy.next


head, _ = createLinkedList([1,2])
n = 1

print(transformToArray(removeNthFromEnd(head, n)))