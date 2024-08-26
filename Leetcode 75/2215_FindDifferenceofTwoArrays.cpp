/**
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

    answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
    answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

Note that the integers in the lists may be returned in any order.

I brute forced this in O(n^2) time 💀
**/
class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        vector<vector<int>> ret;
        vector<int> num1_vec;
        vector<int> num2_vec;

        for (int i = 0; i < nums1.size(); i++) {
            if (find(nums2.begin(), nums2.end(), nums1[i]) == nums2.end()) {
                if (find(num1_vec.begin(), num1_vec.end(), nums1[i]) == num1_vec.end())
                    num1_vec.push_back(nums1[i]);
            }
        }
        for (int i = 0; i < nums2.size(); i++) {
            if (find(nums1.begin(), nums1.end(), nums2[i]) == nums1.end() ) {
                if (find(num2_vec.begin(), num2_vec.end(), nums2[i]) == num2_vec.end())
                    num2_vec.push_back(nums2[i]);
            }
        }

        ret.push_back(num1_vec);
        ret.push_back(num2_vec);

        return ret;
    }
};
