class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def maxSub(subNums, left, right):
            if left > right: 
                return float('-inf')
            
            mid = left + (right - left) // 2
            sum_left, sum_right, sum_cur = 0, 0, 0
            
            for i in range(mid-1,left-1,-1): 
                sum_cur += subNums[i]
                sum_left = max(sum_left, sum_cur)
            
            sum_cur = 0
            
            for j in range(mid + 1, right + 1):
                sum_cur += subNums[j]
                sum_right = max(sum_right, sum_cur)
            
            return max( maxSub(subNums,left,mid -1), maxSub(subNums,mid+1,right), subNums[mid] + sum_left + sum_right)
            
        
        return maxSub(nums, 0, len(nums) - 1)
    