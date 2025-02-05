"""
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.
"""
class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        if s1 == s2:
            return True

        for i in range(len(s1)):
            for j in range(len(s1)):
                s3 = self.swap_chars(s1, i, j)
                if s3 == s2:
                    return True
        return False

    def swap_chars(self, string, i, j):
        """Swaps characters at indices i and j in the given string."""
        return string[:i] + string[j] + string[i+1:j] + string[i] + string[j+1:]
