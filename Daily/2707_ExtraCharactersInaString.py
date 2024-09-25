"""
You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.

"""
class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        n = len(s)
        # Use DP to keep track of minimum remaining characters
        dp = [n + 1] * (n + 1)

        # Base case: no characters, start with 0
        dp[0] = 0

        # build DP table forwards
        for i in range(1, n + 1):
            # Case 1: keep the current character
            dp[i] = dp[i - 1] + 1
            
            # Check each substring to see if it matches ending at the i-th character
            for sub in dictionary:
                sub_len = len(sub)
                if i >= sub_len and s[i - sub_len:i] == sub:
                    # If the substring matches, skip its length
                    dp[i] = min(dp[i], dp[i - sub_len])
        
        return dp[n]
