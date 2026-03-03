from utils.linked_list import ListNode, transformToArray


class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = ListNode(-1)
        self.tail = ListNode(-1)

        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.prep(node)

        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value

            self.prep(node)
            return
        
        if len(self.cache) == self.capacity:
            last = self.tail.prev

            last.prev.next = self.tail
            self.tail.prev = last.prev

            del self.cache[last.key]

        node = ListNode(value, key)
        self.cache[key] = node
        self.prep(node)


    def prep(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node


lru = LRUCache(2)
lru.put(1, 1)
print(transformToArray(lru.head))

lru.put(2, 2)
print(transformToArray(lru.head))

print(lru.get(1))

lru.put(3, 3)
print(transformToArray(lru.head))

print(lru.get(2))

lru.put(4, 4)
print(transformToArray(lru.head))

print(lru.get(1))
print(lru.get(3))
print(lru.get(4))


"""

请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
"""