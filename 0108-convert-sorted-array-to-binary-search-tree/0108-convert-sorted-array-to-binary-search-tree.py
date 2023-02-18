# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums or len(nums) == 0: 
            return None
        
        def toBinarySearchTree(nums, left, right):
            if (left > right): 
                return None
            
            mid = left + (right - left) // 2
            new_node = TreeNode(nums[mid])
            new_node.left = toBinarySearchTree(nums, left, mid -1)
            new_node.right = toBinarySearchTree(nums, mid + 1, right)
            return new_node
        
        return toBinarySearchTree(nums, 0, len(nums) - 1)