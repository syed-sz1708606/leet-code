class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = {} 
        for i, num in enumerate(nums): 
            if target - num in res: 
                return [i, res[target - num]]
            res[num] = i