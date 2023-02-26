"""
Leetcode Problem
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy, sell = 0,1
        profit = 0

        while sell <= len(prices)-1 and buy < sell:
            print(profit)
            profit = max(profit, prices[sell] - prices[buy])
            if prices[sell] < prices[buy]:
                buy = sell
                sell += 1
            else:
                sell += 1
        
        return profit


