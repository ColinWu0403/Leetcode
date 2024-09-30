"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

    For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".

Return the number of different expressions that you can build, which evaluates to target.
"""
import numpy as np

class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        n = len(nums)
        totalSum = sum(nums)
        
        # Check for possible valid range
        if abs(target) > totalSum:
            return 0
        
        # Initialize DP table as the number of ways to achieve a sum j using the first i numbers.
        dp = np.zeros([n + 1, 2*totalSum + 1], dtype=int)

        # since we have 2 times the total to account for negative numbers
        offset = totalSum

        # Base case: one way to reach a sum of 0 with 0 elements
        dp[0][offset] = 1

        for i in range(1, n + 1): # go through each nums
            for j in range(-totalSum, totalSum + 1): # go through all possible sums
                if dp[i - 1][j + offset] > 0:  # Check if the previous state is reachable
                    dp[i][j + nums[i - 1] + offset] += dp[i - 1][j + offset]  # Adding the current number
                    dp[i][j - nums[i - 1] + offset] += dp[i - 1][j + offset]  # Subtracting the current number

        # Using n numbers how many ways we can sum to get the target
        return dp[n][target + offset]
