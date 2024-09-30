"""
You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. The player adds the chosen number to their score. The game ends when there are no more elements in the array.

Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. You may assume that both players are playing optimally.
"""
class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        # Initialize DP table where dp[i][j] stores the maximum  difference on turn i,j
        dp = [[0] * n for _ in range(n)]

        # Base case: there's only one num
        for i in range(n):
            dp[i][i] = nums[i]
        
        # Build DP table
        for k in range(2, n + 1): # Iterate through different lengths (k) of the subarrays of nums
            for i in range(n - k + 1): # finds dp[i][j] for all indices i to end of subarray
                j = i + k - 1
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])
        
        # if difference is greater than or equal to 0, player1 wins
        return dp[0][n - 1] >= 0
