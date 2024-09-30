"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        INF = 10**5
        # Initialize DP table representing the gain/loss for each day if we sell the next
        dp = [0] * (n)

        # Calculate current day profit
        for i in range(n - 1):
            dp[i] = prices[i+1] - prices[i]
        
        res = dp[0]
        maxEnding = dp[0]

        # Find maximum subarray sum (best profit)
        for i in range(1, len(dp)):
            
            maxEnding = max(maxEnding + dp[i], dp[i])
            
            # Update res if maximum subarray sum ending at index i > res
            res = max(res, maxEnding)

        return res
