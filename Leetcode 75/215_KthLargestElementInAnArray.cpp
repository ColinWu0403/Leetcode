/**
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Note: I used quickselect which solves in O(n) average time but for some reason,
leetcode adds a test case with a ridiculous number of elements so that case times out (the worst case runtime would be O(n^2)
**/
class Solution {
public:
    // Randomized partition: shifts all elements smaller than the randomly chosen pivot to the left and larger to the right
    int randPartition(vector<int>& arr, int l, int r) {
        int n = r - l + 1;
        int pivot = rand() % n; // Random pivot
        swap(arr[l + pivot], arr[r]); // Move pivot to the end
        return partition(arr, l, r);
    }

    // Partition in quickselect
    int partition(vector<int>& arr, int l, int r) {
        int pivot = arr[r];
        int i = l;
        for (int j = l; j < r; j++) {
            if (arr[j] <= pivot) {
                swap(arr[i], arr[j]);
                i++;
            }
        }
        swap(arr[i], arr[r]); // Place pivot in its correct position
        return i;
    }

    // Recursive function to find the kth smallest element (quickselect algorithm)
    int quickSelect(vector<int>& nums, int l, int r, int k) {
        if (l <= r) {
            int index = randPartition(nums, l, r);

            // If pivot index is k
            if (index == k) {
                return nums[index];
            }
            // Recurse left subarray
            else if (index > k) {
                return quickSelect(nums, l, index - 1, k);
            }
            // Recurse right subarray
            else {
                return quickSelect(nums, index + 1, r, k);
            }
        }
        return -1; // Should not reach here
    }

    int findKthLargest(vector<int>& nums, int k) {
        return quickSelect(nums, 0, nums.size() - 1, nums.size() - k);
    }
};
