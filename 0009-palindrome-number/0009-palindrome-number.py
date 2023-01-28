class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: 
            return False
        tempX = int(str(x)[::-1])
        return (x - tempX == 0)