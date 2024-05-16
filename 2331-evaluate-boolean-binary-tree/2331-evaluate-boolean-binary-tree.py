# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        # If it's a leaf node, return its value
        if root.left is None and root.right is None:
            return root.val == 1
        
        # Recursively evaluate left and right subtrees
        left_val = self.evaluateTree(root.left)
        right_val = self.evaluateTree(root.right)
        
        # Apply the boolean operation based on the node's value
        if root.val == 2:
            return left_val or right_val
        elif root.val == 3:
            return left_val and right_val
        else:
            return False
        
        