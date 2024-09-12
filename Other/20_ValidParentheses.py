"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        paren_hash = {")" : "(", "}" : "{", "]" : "["}

        for c in s:
            if c in paren_hash:
                if stack and stack[-1] == paren_hash[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        if not stack:
            return True
        else:
            return False
