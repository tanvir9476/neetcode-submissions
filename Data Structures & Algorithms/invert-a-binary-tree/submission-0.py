# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        while not root:
            return None
        # print(root)
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
        


    # # Recursive Pre Order Traversal (DFS) Time: O(n), Space: O(n)
    # def pre_order(node):
    #     if not node:
    #         return
    #     print(node)
    #     node.left, node.right = node.right, node.left
    #     pre_order(node.left)
    #     pre_order(node.right)

    # pre_order(A)