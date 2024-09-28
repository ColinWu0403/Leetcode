/**
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
**/

public class Solution {

    // O(n) Time and O(n) Space Solution
    public int MajorityElement(int[] nums) {
        // Using Dictionary as Hashmap
        Dictionary<int, int> numCounts = new Dictionary<int, int>();
        int result = 0;
        int maxCount = 0;
        foreach (int num in nums) {
            if (!numCounts.ContainsKey(num)) { // key doesn't exist
                numCounts[num] = 0;
            }

            numCounts[num] += 1;

            // Update result if element appears more
            if (numCounts[num] > maxCount) {
                maxCount = numCounts[num];
                result = num;
            }
        }

        return result;
    }

    // O(n) Time and O(1) Space Solution using Boyer-Moore Voting Algorithm
    public int MajorityElementImproved(int[] nums) {

        int result = 0;
        int maxCount = 0;
        foreach (int num in nums) {
            if (maxCount == 0) {
                result = num;
            }
            
            if (num == result) {
                maxCount += 1;
            }
            else {
                maxCount -= 1;
            }
        }

        return result;
    }
}
