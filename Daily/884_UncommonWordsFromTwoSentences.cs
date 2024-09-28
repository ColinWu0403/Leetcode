/**
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
**/
public class Solution {
    public string[] UncommonFromSentences(string s1, string s2) {
        // Use Hashmap to get number of occurences
        Dictionary<string, int> wordCount = new Dictionary<string, int>();

        // Split by spaces
        string[] s1Split = s1.Split(new char[0]);
        string[] s2Split = s2.Split(new char[0]);

        foreach (string word in s1Split) {
            if (wordCount.ContainsKey(word)) {
                wordCount[word]++;
            } else {
                wordCount[word] = 1;
            }
        }

        foreach (string word in s2Split) {
            if (wordCount.ContainsKey(word)) {
                wordCount[word]++;
            } else {
                wordCount[word] = 1;
            }
        }

        // Return all keys with only 1 occurence
        List<string> result = new List<string>();
        foreach (var entry in wordCount) {
            if (entry.Value == 1) {
                result.Add(entry.Key);
            }
        }
        return result.ToArray();
    }
}
