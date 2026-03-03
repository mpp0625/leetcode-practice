from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    
    result = []
    stack = []
    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        node = stack.pop()
        if node.val is not None:
            result.append(node.val)

        curr = node.right

    print(result)


arr = [1,None,2,3]
# arr = [1,2,3,4,5,6,7]
root = TreeNode(arr[0])

stack = [root]
i = 1

while stack and i < len(arr):
    node = stack.pop(0)
    
    node.left = TreeNode(arr[i])
    
    if arr[i]:
        stack.append(node.left)
    i += 1

    if i < len(arr):
        node.right = TreeNode(arr[i])
        if arr[i]:
            stack.append(node.right)
        i += 1

inorderTraversal(root)