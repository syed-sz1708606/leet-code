class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: 
            return s
        
        step =  (numRows - 1) * 2
        str = ""

        for i in range(0, numRows):
            for j in range(i, len(s), step):
                str += s[j]
                if((i > 0) and (i < numRows-1) and (j + step - (2 * i)) < len(s)):
                    str += s[j + step - 2 * i ]
                
                
        return str
        