# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        
        def dfs(node):
            if not node:
                return 0
            
            left_balance = dfs(node.left)
            right_balance = dfs(node.right)
            
            # Current balance: total coins in this subtree minus the number of nodes in this subtree
            balance = node.val + left_balance + right_balance - 1
            
            # The number of moves is increased by the absolute value of the balance
            self.moves += abs(balance)
            
            return balance
        
        dfs(root)
        return self.moves
        