class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needleptr, lptr, rptr = 0, 0, 0
        
        haystack_len = len(haystack)
        needle_len = len(needle)
        
        for i in range(haystack_len):
            if needle_len > haystack_len - i: 
                return -1
            if haystack[i:i + needle_len] == needle: 
                return i
        
        return -1
        