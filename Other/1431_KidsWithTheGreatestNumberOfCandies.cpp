/**
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.
**/
class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int maxCandies = 0;
        for (auto candy : candies) {
            maxCandies = max(maxCandies, candy);
        }

        vector<bool> result;
        for (auto candy : candies) {
            if (candy + extraCandies >= maxCandies) {
                result.push_back(true);
            }
            else {
                result.push_back(false);
            }
        }
        return result;
    }
};
