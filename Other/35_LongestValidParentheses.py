"""
Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses
substring
"""
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        stack = []
        n = len(s)
        bitArray = [0] * n

        for i, c in enumerate(s):
            if c == "(": # start parenthesis
                stack.append(i)
            if c == ")" and stack: # valid end parenthesis, set both array indices to 1
                matchPos = stack.pop()
                bitArray[matchPos] = 1
                bitArray[i] = 1

        maxLen = 0
        curLen = 0
        for num in bitArray: # find longest consecutive repitition of 1s
            if num == 1:
                curLen += 1
                if maxLen < curLen:
                    maxLen = curLen
            else:
                curLen = 0
        return maxLen
