"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
"""
import numpy as np

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        
        # Initialize DP table dp[k, i] where k is the number of transactions (max = 2) and i is the number of days
        dp = np.zeros([3, n]) 
        mink = [prices[0]] * 3

        # For each price, find the 
        for i in range(1, n):
            for k in range(1, 3):
                # Find minimum transaction cost for each transaction
                mink[k] = min(mink[k], prices[i] - dp[k-1, i-1])

                # Find max profit between previous day and the profit if we're selling today
                dp[k, i] = max(dp[k, i-1], prices[i] - mink[k])
        
        # return last transaction done of the last day
        return int(dp[2, n - 1])
