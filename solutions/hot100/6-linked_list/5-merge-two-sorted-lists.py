from typing import Optional

from utils.linked_list import ListNode, createLinkedList, transformToArray


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 and list2:
        currA, currB = list1, list2

        if list1.val <= list2.val:
            currA = list1
            currB = list2
        else:
            currA = list2
            currB = list1

        node = currA
        curr = node

        while currA:
            currNext = currA.next

            if currNext.val <= currB.val:
                curr.next = currNext
                currA = currNext
            else:
                curr.next = currB
                currB = currB.next
            
            curr = curr.next

        curr.next = currB
        
        return node
    else:
        return list1 or list2


l1 = [1,2,4]
l2 = [1,3,4]

head1, _ = createLinkedList(l1)
head2, _ = createLinkedList(l2)

print(transformToArray(mergeTwoLists(head1, head2)))