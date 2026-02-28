from typing import List, Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def createLinkedList(arr: List) -> Optional[ListNode]:
    if not arr:
        return None, None
    
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


def findNodeByPos(head: Optional[ListNode], pos: int):
    if not head:
        return None
    
    if pos == -1:
        return None

    begin = 0

    current = head
    while current:
        if begin == pos:
            return current
        
        current = current.next
        begin += 1
    
    return None


def reverseLinkedList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head

    while curr:
        next_node = curr.next
        
        curr.next = prev
        prev = curr

        curr = next_node

    return prev


def transformToArray(head: Optional[ListNode]) -> List:
    if not head:
        return []
    
    arr = []
    curr = head

    while curr:
        arr.append(curr.val)
        curr = curr.next

    return arr