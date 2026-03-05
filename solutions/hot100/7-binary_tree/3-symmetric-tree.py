from typing import Optional

from utils.binary_tree import TreeNode, creatBinaryTree


def isSymmetric(root: Optional[TreeNode]) -> bool:
    if not root:
        return False
    
    stack = [(root.left, root.right)]

    while stack:
        left, right = stack.pop(0)

        if left is None and right is None:
            continue

        if bool(left) != bool(right):
            return False

        if left.val != right.val:
            return False
        
        stack.append((left.left, right.right))
        stack.append((left.right, right.left))

    return True


arr = [2,3,3,4,5,5,4,None,None,8,9,9,8]
print(isSymmetric(creatBinaryTree(arr)))