from typing import Optional

from utils.linked_list import ListNode, createLinkedList, reverseLinkedList


def isPalindrome1(head: Optional[ListNode]) -> bool:
    if not head:
        return False
    
    s, f = head, head

    while s.next and f.next and f.next.next:
        s = s.next
        f = f.next.next

    first, second = head, reverseLinkedList(s.next)

    while second:
        if first.val != second.val:
            return False
        
        first = first.next
        second = second.next

    return True


def isPalindrome2(head: Optional[ListNode]) -> bool:
    front = head

    def recursively_check(node):
        nonlocal front

        if not node:
            return True
        
        if not recursively_check(node.next):
            return False
        
        if node.val != front.val:
            return False
        
        front = front.next

        return True

    return recursively_check(head)


head, _ = createLinkedList([1,2,2,1])
print(isPalindrome2(head))


"""
转数组 + 双指针:
    将链表转成数组，然后使用双指针 left = 0 right = n - 1;
    时间复杂度 O(n)，空间复杂度 O(n)

isPalindrome2 快慢指针 + 链表反转：
    核心问题：找到中心位置；
    快慢指针：慢指针每次变化 next，快指针每次变化 next.next，这样当快指针遍历完成后慢指针刚好进行到一半剩下的是后半部分；

    将慢指针反转，遍历与 head 进行比较；时间复杂度 O(n)，空间复杂度 O(1)

isPalindrome2 递归:
    根据递归`先进后出`的特性，模拟从两端向中间比较。
    递归到链表末尾，回溯（从后向前）与 head （从前向后）进行比较。
"""