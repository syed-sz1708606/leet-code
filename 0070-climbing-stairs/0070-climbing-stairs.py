class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: 
            return 1
        elif n == 2: 
            return 2
        
        dp = [0] * (n+1)
        
        dp[-1] = 1
        dp[-2] = 1
        
        
        for i in range(n-2, -1, -1): 
            dp[i] = dp[i+1] + dp[i+2]
            
        return dp[0]