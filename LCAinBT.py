#leetcode:accepted
#time complexity: O(N)
#pace;O(1)
#explination: you need to keep finding the left and right child of every root and check if the values are equal to the values of p and q


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root==None or root==p or root==q:
            return root
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        if left!=None and right!=None:
            return root
        elif left!=None:
            return left
        elif right!=None:
            return right
        else:
            return None