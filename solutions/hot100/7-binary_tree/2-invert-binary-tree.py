from typing import Optional

from utils.binary_tree import TreeNode, creatBinaryTree


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    
    stack = [root]

    while stack:
        node = stack.pop(0)
        node.left, node.right = node.right, node.left

        if node.left:
            stack.append(node.left)
        
        if node.right:
            stack.append(node.right)
    
    return root


arr = [2,1,3]
invertTree(creatBinaryTree(arr))