from typing import Optional

from utils.linked_list import ListNode, createLinkedList, findNodeByPos


def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    s, f = head, head

    while f and f.next:
        s = s.next
        f = f.next.next

        if s == f:
            p = head

            while p != s:
                p = p.next
                s = s.next

            return p

    return None


arr = [3,2,0,-4]
pos = 1

head, current = createLinkedList(arr)
current.next = findNodeByPos(head, pos=pos)

print(detectCycle(head))


"""
快慢指针：
    设 0 ~ pos 的长度为 a, pos ~ 快慢指针相交点的长度为 b, 快慢指针相交点 ~ pos 的长度为 c；
    以 arr = [3,2,0,-4]  pos = 1 快慢指针相交点在 -4 为例，a=1 b=2 c=；

    至相交点时，快指针走的距离为 a + n(b + c) + b，慢指针走的距离时 a + b，由于快指针是慢指针速度的2倍，所以：
        a + n(b + c) + b = 2(a + b) 经过系列变换得到 a = (n - 1)(b + c) + c

    所以再次定义一个指针从 head 头开始，当走的距离为 a 时，它与慢指针会相遇，两个指针的变化都是每次一步；

哈希表：
    也可以实现，并且容易理解，但是它的空间复杂度为 O(n)；
"""