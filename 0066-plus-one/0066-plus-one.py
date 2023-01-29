class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if(digits[0] == 0): 
            return [1]
        
        num = int("".join(str(i) for i in digits)) + 1
        result = []
        
        for i in str(num):
            result.append(int(i))
        return result
        