"""
You are given a string s consisting of the characters 'N', 'S', 'E', and 'W', where s[i] indicates movements in an infinite grid:

    'N' : Move north by 1 unit.
    'S' : Move south by 1 unit.
    'E' : Move east by 1 unit.
    'W' : Move west by 1 unit.

Initially, you are at the origin (0, 0). You can change at most k characters to any of the four directions.

Find the maximum Manhattan distance from the origin that can be achieved at any time while performing the movements in order.
The Manhattan Distance between two cells (xi, yi) and (xj, yj) is |xi - xj| + |yi - yj|. 
"""
class Solution(object):
    def maxDistance(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxDist = 0
        x = y = 0
        for i in range(len(s)):
            if s[i] == 'N':
                y += 1
            elif s[i] == 'S':
                y -= 1
            elif s[i] == 'E':
                x += 1
            elif s[i] == 'W':
                x -= 1

            maxDist = max(maxDist, min(abs(y) + abs(x) + k * 2, i + 1))
        return maxDist
