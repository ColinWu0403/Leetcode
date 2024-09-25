"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # Initialize DP table where DP[n+3] = DP[n] + DP[n+1] + DP[n+2]
        dp = [n + 1] * (n + 1)

        # Base cases
        if n == 0:
            return 0
        elif n == 1 or n == 1:
            return 1
    
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        # Build DP table forwards
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        
        return dp[n]
