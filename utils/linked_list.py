from typing import List, Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def createLinkedList(arr: List) -> Optional[ListNode]:
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head
    
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next

    return head, current


def createIntersectingLists(
    listA: List[int], 
    listB: List[int], 
    skipA: int, 
    skipB: int
):
    if not listA or not listB:
        return None, None

    headA, currentA = createLinkedList(listA[: skipA])
    headB, currentB = createLinkedList(listB[: skipB])

    if skipA < len(listA):
        intersection = ListNode(listA[skipA])
        currentA.next = intersection
        currentB.next = intersection
    
    return headA, headB