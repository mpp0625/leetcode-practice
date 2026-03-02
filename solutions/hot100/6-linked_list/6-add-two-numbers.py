from typing import Optional

from utils.linked_list import ListNode, createLinkedList, transformToArray


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(-1)
    curr = dummy

    q = 0

    while l1 or l2:
        s = 0

        if l1:
            s += l1.val
            l1 = l1.next

        if l2:
            s += l2.val
            l2 = l2.next

        q, r = divmod(s + q, 10)
        curr.next = ListNode(r)

        curr = curr.next

    if q:
        curr.next = ListNode(q)

    return dummy.next


l1 = [2,4,3]
l2 = [5,6,4]

head1, _ = createLinkedList(l1)
head2, _ = createLinkedList(l2)

print(transformToArray(addTwoNumbers(head1, head2)))