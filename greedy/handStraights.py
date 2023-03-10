"""
Leetcode Problem
https://leetcode.com/problems/hand-of-straights/
"""

class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        if not (len(hand) % groupSize == 0):
            return False
        
        countCards = {}
        for card in hand:
            countCards[card] = 1 + countCards.get(card, 0)
    
        numberOfGroups = len(hand) // groupSize

        for i in range(numberOfGroups):
            val1 = min(countCards.items())[0]
            countCards[val1] -= 1
            if countCards[val1] == 0: del countCards[val1]

            for i in range(1, groupSize):
                val = val1 + i
                if val in countCards:
                    countCards[val] -= 1
                    if countCards[val] == 0: del countCards[val]
                else:
                    return False
        
        return True
