# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def traverse(root):    
            if not root:
                return True, 0
            else:
                left_tree = traverse(root.left)
                right_tree = traverse(root.right)
                valid_tree = abs(left_tree[1] - right_tree[1]) < 2 and left_tree[0] and right_tree[0]
                return valid_tree, 1 + max(left_tree[1],  right_tree[1])
        
        return traverse(root)[0]