/**
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
**/
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int len1 = word1.length();
        int len2 = word2.length();
        int total = len1 + len2;
        string ret;

        int i = 0;
        int j = 0;
        int k = 0;
        while (i < total) {
            if (j >= len1) {
                ret += word2.substr(k);
                break;
            }
            else if (k >= len2) {
                ret += word1.substr(j);
                break;
            }
            else {
                if (i % 2 == 0) {
                    ret += word1[j];
                    j++;
                }
                else {
                    ret += word2[k];
                    k++;
                }

            }
            i++;
        }
        return ret;
    }
};
