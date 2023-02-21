class Solution {
    public int maxSubArray(int[] nums) {
        int cur_max = nums[0]; 
        int glob_max = nums[0];
        int nums_length = nums.length;
            
        for (int i = 1; i < nums_length; i++) {
            cur_max = Math.max(nums[i], cur_max + nums[i]); 
            
            if(cur_max > glob_max)
                glob_max = cur_max; 
        }
        
        return glob_max;
        
    }
}