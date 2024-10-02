# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from idlelib.tree import TreeNode
from typing import Optional


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_sum = float(0) # smallest possible value
        max_level = 1 # max sum of nodes at a level
        current_level = 1 # root level start

        queue = deque([root]) # queue to perform BFS ( store nodes level by level), what is deque, how does it work?

        while queue:
            level_sum = 0 # sum of all nodes at the current level
            level_size = len(queue) # Number of nodes at the current level, why use len() here

            # perform level-order traversal -- BFS
            for _ in range(level_size):
                node = queue.popleft() # what is this popleft() does here?
                level_sum += node.val  # add the node's value to the level sum, how is this summing the both
                # node.vals, how does it work?

                # add the child nodes to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # if this level's sum is greater than the max_sum, we update it here
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level

            # Move to the next level
            current_level += 1

        return max_level
