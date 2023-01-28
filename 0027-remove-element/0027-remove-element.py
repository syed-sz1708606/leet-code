class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        for v in nums: 
            if v != val: 
                nums[j] = v
                j = j + 1
        return j