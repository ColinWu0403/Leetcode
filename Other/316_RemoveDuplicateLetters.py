"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is
the smallest in lexicographical order
among all possible results.

 

Example 1:

Input: s = "bcabc"
Output: "abc"

Example 2:

Input: s = "cbacdcbc"
Output: "acdb"
"""
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        added = set()

        occurs = {char: 0 for char in s}
        for char in s:
            occurs[char] += 1
        
        for char in s:
            occurs[char] -= 1

            if char in added:
                continue
            
            while stack and char < stack[-1] and occurs[stack[-1]] > 0:
                removed_char = stack.pop()
                added.remove(removed_char)
            
            stack.append(char)
            added.add(char)
        
        return "".join(stack)
