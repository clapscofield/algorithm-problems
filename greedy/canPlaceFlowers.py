"""
Leetcode Problem
https://leetcode.com/problems/can-place-flowers/
"""

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        
        i = 0

        newarray = []
        newarray.append(0)
        for i in range(len(flowerbed)):
            newarray.append(flowerbed[i])
        newarray.append(0)

        for i in range(1, len(flowerbed)+1):
            if newarray[i] == 0 and newarray[i-1] == 0 and newarray[i+1] == 0:
                newarray[i] = 1
                n -= 1
            #print(newarray)

        return True if n <= 0 else False
