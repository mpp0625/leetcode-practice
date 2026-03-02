from typing import Optional

from utils.linked_list import ListNode, createLinkedList, transformToArray


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(-1)
    curr = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        
        curr = curr.next

    curr.next = list1 or list2

    return dummy.next


l1 = [1,2,4]
l2 = [1,3,4]

head1, _ = createLinkedList(l1)
head2, _ = createLinkedList(l2)

print(transformToArray(mergeTwoLists(head1, head2)))
