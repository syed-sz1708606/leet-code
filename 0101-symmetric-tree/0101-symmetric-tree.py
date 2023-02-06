# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def symmetrical(t1, t2): 
            if t1 == None and t2 == None: 
                return True
            if t1 == None or t2 == None: 
                return False
            
            return (t1.val == t2.val) and symmetrical(t1.left, t2.right) and symmetrical(t1.right, t2.left)
        
        return symmetrical(root, root)