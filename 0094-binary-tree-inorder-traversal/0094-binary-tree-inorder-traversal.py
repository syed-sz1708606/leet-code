# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def inorder(p):
            if p.left: 
                inorder(p.left)
            res.append(p.val)
            if p.right: 
                inorder(p.right)
            
        if root:
            inorder(root)
        
        return res
    
    