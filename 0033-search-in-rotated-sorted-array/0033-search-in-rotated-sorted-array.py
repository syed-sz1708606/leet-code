class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums_len = len(nums)
        low, high = 0, nums_len - 1
        
        while low <= high: 
            mid = low + (high - low) // 2
            
            if nums[mid] == target: 
                return mid
            elif nums[low] <= nums[mid]:
                if nums[low] <= target and target <= nums[mid]:
                    high = mid - 1
                else: 
                    low = mid + 1
            else:
                if nums[mid] <= target and target <= nums[high]: 
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
            
        