"""
Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1.
"""
class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Use Divide and Conquer to recursively calculate the maximum difference
        return self.divideConquerMax(nums, 0, len(nums) - 1)

    def divideConquerMax(self, nums, start, end):
        if start == end:
            return -1
        
        # Divide: split array into 2 halves
        mid = (start + end) // 2
        
        # Conquer: Recursively solve for left and right halves + between the two
        maxDiffLeft = self.divideConquerMax(nums, start, mid)
        maxDiffRight = self.divideConquerMax(nums, mid + 1, end)
        
        # Overall maximum difference
        minLeft = min(nums[start:mid + 1]) # minimum in left half
        maxRight = max(nums[mid + 1:end + 1]) # maximum in right half

        # Calculate the cross difference if valid
        crossDiff = -1
        if maxRight > minLeft: # Check if valid
            crossDiff = maxRight - minLeft
        
        maxDiff = max(maxDiffLeft, maxDiffRight, crossDiff)
        
        # If no valid maxDiff, return -1
        if maxDiff <= 0:
            return -1
        
        return maxDiff
