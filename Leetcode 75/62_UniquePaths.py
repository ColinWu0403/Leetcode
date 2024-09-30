"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 10^9.
"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        # Initialize DP table, it represents all ways to reach column n in a row
        dp = [0] * n

        # Base Case: top left corner -> 1 way to reach
        dp[0] = 1

        for i in range(m): # for each row 
            for j in range(1, n): # for each column j in row i
                dp[j] += dp[j - 1] # add the ways to reach the previous column

        return dp[n - 1]
