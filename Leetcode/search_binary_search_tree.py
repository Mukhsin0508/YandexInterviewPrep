# Key Points of a Binary Search Tree:
# Left subtree < Root < Right subtree for all nodes.
# The in-order traversal of a BST (left, root, right) will always give you the nodes'
    # values in sorted (increasing) order.
from contextlib import nullcontext
# ================ My Approach ==============
# We can take advantage of the BST's properties to perform a binary search. Starting from the root:
# If the root’s value matches the target val, return the root.
# If the target value is smaller than the current node’s value, move to the left subtree (root.left).
# If the target value is larger than the current node’s value, move to the right subtree (root.right).
# If we reach a null node without finding the value, return null (indicating the value doesn’t exist in the tree).

from idlelib.tree import TreeNode
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Base case: If root is null or we've found the node with value == val
        if root is None or root.val == val:
            return root

        # If the target value is less than the root's value, search in the left subtree
        if val < root.val:
            return self.searchBST(root.left, val)

        # If the target value is greater than the root's value, search in the right subtree
        return self.searchBST(root.right, val)

    # Helper function to serialize the tree (convert it to list representation)
    def serialize(self, root: TreeNode):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)

        # Remove trailing None values (for cleaner output)
        while result and result[-1] is None:
            result.pop()

        return result
