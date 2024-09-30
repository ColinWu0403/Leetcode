"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Note: This implementation is a bit faster (O(nlogn)) than brute force but it's not good lol.

I used Divide and Conquer to solve it as review for my Algorithms Exam, for the most efficient solution in O(n), use Kadane's Algorithm:
https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            return nums[0]

        # Divide: split array into two halves
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        # Conquer: recursively find the maximum subarray in each half
        leftMSA = self.maxSubArray(left)
        rightMSA = self.maxSubArray(right)

        # Max subarray might be between the two halves
        midMSA = self.maxSubArrayMid(nums, mid)

        return max(leftMSA, rightMSA, midMSA)

    def maxSubArrayMid(self, nums, mid):

        # Find the maximum sum starting from the middle to the left
        leftSum = float('-inf')
        currSum = 0
        for i in range(mid - 1, -1, -1):
            currSum += nums[i]
            leftSum = max(leftSum, currSum)

        # Find the maximum sum starting from the middle to the right
        rightSum = float('-inf')
        currSum = 0
        for i in range(mid, len(nums)):
            currSum += nums[i]
            rightSum = max(rightSum, currSum)

        # Combine the left and right sums to get the crossing sum
        return leftSum + rightSum
