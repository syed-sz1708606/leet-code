class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        htable = {} 
        
        for num in nums: 
            if num not in htable: 
                htable[num] = 1
            else: 
                htable[num] = htable[num] + 1
        
        htable = sorted(htable.items(), key= lambda item: item[1], reverse=True)

        res = [item[0] for item in htable[:k]]
        
        return res
            
