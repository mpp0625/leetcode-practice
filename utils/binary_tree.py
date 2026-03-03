from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def creatBinaryTree(arr: List) -> Optional[TreeNode]:
    if not arr:
        return None

    root = TreeNode(arr[0])

    stack = [root]
    i = 1

    while stack and i < len(arr):
        node = stack.pop(0)
        
        if arr[i] is not None:
            node.left = TreeNode(arr[i])
            stack.append(node.left)
        i += 1

        if i < len(arr):
            if arr[i] is not None:
                node.right = TreeNode(arr[i])
                stack.append(node.right)
            i += 1

    return root