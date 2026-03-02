from typing import Optional

from utils.linked_list import ListNode


def copyRandomList1(head: Optional[ListNode]) -> Optional[ListNode]:
    def getNodes(head: Optional[ListNode]):
        nodes = []
        copyNodes = []

        while head:
            nodes.append(head)
            copyNodes.append(ListNode(head.val))

            head = head.next

        return nodes, copyNodes

    if not head:
        return head
    
    nodes, copyNodes = getNodes(head)

    for i, n in enumerate(nodes):
        nextNode = n.next
        if nextNode:
            index = nodes.index(nextNode)
            copyNodes[i].next = copyNodes[index]

        randomNode = n.random
        if randomNode:
            index = nodes.index(randomNode)
            copyNodes[i].random = copyNodes[index]

    return copyNodes[0]


def copyRandomList2(head: Optional[ListNode]) -> Optional[ListNode]:
    hashmap = {}
    curr = head

    while curr:
        hashmap[curr] = ListNode(curr.val)
        curr = curr.next

    dummy = ListNode(0)
    prev = dummy
    curr = head

    while curr:
        node = hashmap.get(curr)
        node.random = hashmap.get(curr.random, None)
        prev.next = node

        curr = curr.next
        prev = prev.next
    
    return dummy.next


def copyRandomList3(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head
    
    curr = head
    while curr:
        node = ListNode(curr.val)
        node.next = curr.next
        curr.next = node

        curr = node.next

    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next

        curr = curr.next.next

    prev, curr, headNew = head, head.next, head.next
    while curr.next:
        prev.next = prev.next.next
        curr.next = curr.next.next

        prev = prev.next
        curr = curr.next

    return headNew


l = [[7,1],[13,0],[11,4],[10,2],[1,0]]
head = ListNode(l[0][0])
curr = head

arr = [head]

for i in range(1, len(l), 1):
    node = ListNode(l[i][0])

    curr.next = node
    curr = node

    arr.append(node)

for i in range(len(l)):
    r = l[i][1]

    if r != None:
        arr[i].random = arr[r]
    else:
        arr[i].random = None


print(copyRandomList3(head))


"""
copyRandomList2 哈希表：
    先遍历一遍链表 head 生成哈希表，它以 head 原节点为 key，以重新创建的 ListNode 节点为 value；
    再次遍历 head 使用哈希表的键值生成新的链表；
    时间复杂度：O(n)；空间复杂度：O(n)；

copyRandomList3 拼接 + 拆分：
    先将原始节点与新节点拼接成一个链表：A -> A' -> B -> B' -> C -> C'...
    遍历新的链表，构建新节点的 random
    对新链表进行拆分，分成旧链表和新链表；此处注意一定要先对旧链表进行变化否则会影响链表的节点，以下面为例：
        head = 7 -> 13 -> 11 -> 10 -> 1
        headSplice = 7 -> 7' -> 13 -> 13' -> 11 -> 11' -> 1-> 1'
        
        期望拆分后的链表为:
            headSplit1 = 7 -> 13 -> 11 -> 10 -> 1
            headSplit2 = 7' -> 13' -> 11' -> 10' -> 1'

        假设先对 curr 进行变化（下面是 headSplice 的变化）：
            迭代1：
                curr 变化后 7 -> 7' -> 13' -> 11 -> 11' -> ...
                prev 变化后 7 -> 13' -> 11 -> 11' -> ...
            迭代2：
                curr 变化后 7 -> 13' -> 11 -> 11' -> ...
                prev 变化后 7 -> 13' -> 10 -> 10' -> ...
        
        正确的是先对 prev 进行变化（因为 prev 变化后并不会影响 curr.next.next 的变化，因为 curr 已知在 prev 后）：
            迭代1：
                prev 变化后 7 -> 13 -> 13' -> 11 -> 11' -> ...
                curr 变化后 7 -> 13 -> 13' -> 11 -> 11' -> ...
            迭代2：
                prev 变化后 7 -> 13 -> 11 -> 11' -> ...
                curr 变化后 7 -> 13 -> 11 -> 11' -> ...
"""