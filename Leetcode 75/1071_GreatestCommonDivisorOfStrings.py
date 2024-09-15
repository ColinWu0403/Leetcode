"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""
import math

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str1 + str2 != str2 + str1:
            return ""
        
        # Step 2: Find the GCD of the lengths of the two strings
        gcd_len = self.gcd(len(str1), len(str2))
        
        # Step 3: Return the substring of length gcd_len from str1
        return str1[:gcd_len]

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
