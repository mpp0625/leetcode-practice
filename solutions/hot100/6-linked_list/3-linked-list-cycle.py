from typing import Optional

from utils.linked_list import ListNode, createLinkedList, findNodeByPos

def hasCycle1(head: Optional[ListNode]) -> bool:
    if not head:
        return False

    s, f = head, head.next

    while s != f:
        if not f or not f.next:
            return False

        s = s.next
        f = f.next.next

    return True


def hasCycle2(head: Optional[ListNode]) -> bool:
    current = head

    hashmap = set()

    while current:
        if current in hashmap:
            return True
        
        hashmap.add(current)
        current = current.next
    
    return False


arr = [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]
pos = 8

head, current = createLinkedList(arr)
current.next = findNodeByPos(head, pos=pos)

print(hasCycle2(head))

"""
注意：
    当 pos = n - 1 时，时环形的；
    当 pos = -1 时，是无环的；这一点我最初没有从题目中理解，以为 -1 是连接到最后一个元素，与 n - 1 一样；

hasCycle1 快慢指针：
    原理：如果是环形的快慢指针的 next 永远不可能是 None，它们迟早都会相遇；
    时间复杂度：O(n)；空间复杂度：O(1);

hasCycle2 哈希表：
    原理：将遍历过的节点存储到哈希表中，如果节点已经存在与哈希表中，那么就是环形；
    时间复杂度：O(n)；空间复杂度：O(n);
"""