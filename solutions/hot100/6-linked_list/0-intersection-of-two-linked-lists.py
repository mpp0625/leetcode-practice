from typing import Optional

from utils.linked_list import ListNode, createIntersectingLists


def getIntersectionNode1(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    if not headA or not headB:
        return None

    A, B = headA, headB

    while A != B:
        A = A.next if A else headB
        B = B.next if B else headA

    return A


def getIntersectionNode2(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    hashmap = set()

    temp = headA
    while temp:
        hashmap.add(temp)
        temp = temp.next

    temp = headB
    while temp:
        if temp in hashmap:
            return temp

        temp = temp.next

    return None


intersectVal = 2

listA = [1,9,1,2,4]
listB = [3,2,4]
skipA = 3
skipB = 1

headA, headB = createIntersectingLists(listA, listB, skipA, skipB)
print(getIntersectionNode1(headA, headB))


"""
getIntersectionNode1 双指针法：
    在同一位置相交：
        假设 headA 相交前有 a 个节点，headB 相交前有 b 个节点，相交 c 个节点
        [1,9,1,2,4] + [3,2,4]: 移动 a + b 次
        [3,2,4] + [1,9,1,2,4]: 移动 b + a 次
    
    A、B 相当于两个指针：
        A 指向 headA，当 A 不为空时，将指针 A 挪到下一个节点 (next)；当 A 为空时，将指针移动到 headB；指针 B 同理。

    时间复杂度：O(m + n)，空间复杂度：O(1)


getIntersectionNode2 哈希集合：
    将链表 headA 的所有节点存储在集合中，遍历 headB 判断节点是否在 hash 中
    时间复杂度：O(m + n)，空间复杂度：O(m)
"""