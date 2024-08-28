"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
"""
from collections import defaultdict

class Solution(object):
    def uniqueOccurrences(self, arr):

        occ = defaultdict(int)
        for i in range(len(arr)):
            occ[arr[i]] += 1
        
        uniqueOcc = set([])

        for i in occ:
            if (occ[i] in uniqueOcc):
                return False
            else:
                uniqueOcc.add(occ[i])
        
        return True
        
