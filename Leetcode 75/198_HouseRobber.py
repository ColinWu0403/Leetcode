"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n <= 2:
            return max(nums)
    
        # Initialize DP tables with 0s
        dp = [0] * (n + 1)
        dp[1] = nums[0]
        dp[2] = nums[1]

        # Fill tables from n to 1
        for i in range(2, n):
            dp[i+1] = max(dp[i-1] + nums[i], dp[i-2] + nums[i])
        
        return max(dp)
