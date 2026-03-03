from typing import List, Optional

from utils.binary_tree import TreeNode, creatBinaryTree


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

    return result


# arr = [1,None,2,3]
arr = [1,2,3,4,5,6,7]

inorderTraversal(creatBinaryTree(arr))