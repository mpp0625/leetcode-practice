from typing import Optional

from utils.linked_list import ListNode, createLinkedList, transformToArray


def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    hashmap = {}

    curr = head
    while curr:
        if curr.val in hashmap:
            hashmap[curr.val].append(curr)
        else:
            hashmap[curr.val] = [curr]

        curr = curr.next

    hashmap = dict(sorted(hashmap.items()))

    dummy = ListNode(-1)
    curr = dummy
    for _, nodes in hashmap.items():
        for n in nodes:
            curr.next = n
            curr = n

    curr.next = None

    return dummy.next


def sortList2(head: Optional[ListNode]) -> Optional[ListNode]:
    def divideFunc(head: Optional[ListNode]):
        if not head or not head.next:
            return head

        s ,f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next

        m = s.next
        s.next = None
        return mergeFunc(divideFunc(head), divideFunc(m))

    def mergeFunc(head1: ListNode, head2: ListNode):
        dummy = ListNode(0)
        curr = dummy

        while head1 and head2:
            if head1.val <= head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            
            curr = curr.next

        curr.next = head1 or head2
        return dummy.next
    
    headSorted = divideFunc(head)
    return headSorted


def sortList3(head: Optional[ListNode]) -> Optional[ListNode]:
    def mergeFunc(l1: ListNode, l2: ListNode):
        dummy = ListNode(-1)
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next

        curr.next = l1 or l2
        return dummy.next

    length = 0
    curr = head

    while curr:
        length += 1
        curr = curr.next

    dummy = ListNode(-1, head)
    subLength = 1

    while subLength < length:
        prev, curr = dummy, dummy.next

        while curr:
            head1 = curr

            for _ in range(1, subLength):
                if curr.next:
                    curr = curr.next
                else:
                    break

            head2 = curr.next
            curr.next = None
            curr = head2

            for _ in range(1, subLength):
                if curr and curr.next:
                    curr = curr.next
                else:
                    break

            succ = None
            if curr:
                succ = curr.next
                curr.next = None
                curr = succ

            merged = mergeFunc(head1, head2)
            prev.next = merged

            while prev.next:
                prev = prev.next

        subLength *= 2

    return dummy.next


head, _ = createLinkedList([-1,5,3,4,0])
sortList3(head)
# print(transformToArray(sortList(head)))


"""
mergeTwoLists1 哈希存储 + 排序 -> 链表：
    以值为 key， 将相同值的节点存储到对应的数组中；对 hash 按照 key 进行排序；重新构建链表；
    时间复杂度：O(nlogn)；空间复杂度：O(n)；

    其中 sort 的时间复杂度是 O(klogk) （在本例中 k <= n, k 是 hash 列表的长度）；

mergeTwoLists2 自顶向下归并排序：
    先进行拆分：使用快慢指针将 head 拆分成前半部和后半部两部分，然后持续使用递归拆分直到单个节点
    合并并排序：逐层拆分后得到的数据一层层向前回溯合并

    说明：
        在上面的递归中，永远都会先执行拆分出来的左半部分，因为在方法中它写在了前面， 也就是 `mergeFunc(divideFunc(head), divideFunc(m))` 中的 `divideFunc(head)`；
        直到左半部分全部拆分成了单个节点，如果某一层待合并的全部是单个节点则开始 merge；merge 后如果遇到了待合并的右半部分则开始拆分它们，拆分之后再 merge

    例子：[4,2,1,3]
        1) divide(4,2,1,3) -> left: 4,2  right: 1,3
        2) divide(4,2) -> left: 4  right 2
        3) divide(4) -> return 4
        4) divide(2) -> return 2
        5) merge(4,2) -> sort: 2 -> 4
        6) divide(1,3) -> left: 1  right: 3
        7) divide(1) -> return 1
        8) divide(3) -> return 3
        9) merge(1,3) -> sort: 1 -> 3
        10) merge((2,4), (1,3)) -> sort: 1 -> 2 -> 3 -> 4

    时间复杂度: O(nlog(n))； 空间复杂度: O(log(n)) 递归调用的栈空间；


mergeTwoLists3 自定向下归并排序：
"""