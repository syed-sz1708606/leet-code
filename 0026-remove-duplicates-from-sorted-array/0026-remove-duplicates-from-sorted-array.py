class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        if n == 1: 
            return 1 
        
        new_val = 0
        
        for i in range(1, n): 
            if nums[i] != nums[new_val]: 
                new_val = new_val + 1
                nums[new_val] = nums[i]
        
        return new_val + 1