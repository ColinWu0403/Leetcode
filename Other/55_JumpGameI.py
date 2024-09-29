"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        dp = [False] * (n)

        # Base case:
        dp[0] = True

        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if nums[j] >= i - j and dp[j]:
                    dp[i] = True
                    break
        return dp[-1]
