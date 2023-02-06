class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c = 0
        d = 0
        ind_a = len(a) - 1
        ind_b = len(b) - 1

        for i in range(ind_a, -1, -1): 
            if a[i] == "1":
                c += 2**(abs(i - ind_a))

        for i in range(ind_b, -1, -1): 
            if b[i] == "1": 
                d += 2**(abs(i - ind_b))

        return bin(c + d)[2:]