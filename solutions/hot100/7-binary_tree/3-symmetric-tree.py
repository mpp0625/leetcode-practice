from typing import Optional

from utils.binary_tree import TreeNode, creatBinaryTree


def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    if not root:
        return False


arr = [1,2,2,3,4,4,3]
isSymmetric(creatBinaryTree(arr))