"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
"""
class Solution(object):
    def isSubsequence(self, s, t):

        if len(s) == 0:
            return True
    
        s_index = 0
        s_str = ""
        for t_char in t:
            if s_index == len(s):
                break
            
            if s[s_index] == t_char:
                s_index += 1
                s_str += t_char
        
        if s_str == s:
            return True
        else:
            return False
        
