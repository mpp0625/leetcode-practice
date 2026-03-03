from typing import Optional

from utils.binary_tree import TreeNode, creatBinaryTree


def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    stack = [root]
    deep = 0                   

    while stack:
        dummy = []
        while stack:
            node = stack.pop()
            if node.left is not None:
                dummy.append(node.left)
            if node.right is not None:
                dummy.append(node.right)

        stack = dummy
        deep += 1
    
    return deep


arr = [1,None,2]
arr = [3,9,20,None,None,15,7]

maxDepth(creatBinaryTree(arr))