/**
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
**/

using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public double FindMaxAverage(int[] nums, int k) {
        // Initialize the sum of the first subarray
        double currentSum = 0;
        for (int i = 0; i < k; i++) {
            currentSum += nums[i];
        }

        double maxAverage = currentSum / k;

        // Slide the window across the array
        for (int i = k; i < nums.Length; i++) {
            currentSum += nums[i] - nums[i - k];
            double currentAverage = currentSum / k;
            if (currentAverage > maxAverage) {
                maxAverage = currentAverage;
            }
        }

        return maxAverage;
    }
}
