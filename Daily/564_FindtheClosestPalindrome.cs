/**
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

This question was hard af, way too many stupid edge cases >:(
**/
public class Solution {
    public string NearestPalindromic(string n) {
        int length = n.Length;
        // Case 1: if n is a single-digit number, return n - 1
        if (length == 1) {
            int num = Convert.ToInt32(n);
            if (num == 0) return "0"; // Special case for 0
            return (num - 1).ToString();
        }
        
        // Case 2: Powers of 10, return n - 1
        if (IsPowerOfTen(n)) return (Convert.ToInt64(n) - 1).ToString();
        
        // Initialize possible candidates
        var candidates = new List<long>();

        // Consider other edge cases as candidates
        candidates.Add((long)Math.Pow(10, length) + 1); // e.g., 1000...0001
        candidates.Add((long)Math.Pow(10, length - 1) - 1); // e.g., 999...999
        
        // Middle position index
        int middle = (length + 1) / 2;

        // Extract the prefix and create three variations, 
        long prefix = long.Parse(n.Substring(0, middle));
        for (long i = -1; i <= 1; i++) {
            long newPrefix = prefix + i;
            string palin = createPalindrome(newPrefix.ToString(), length % 2 == 0);
            candidates.Add(long.Parse(palin));
        }
  
        long originalNumber = long.Parse(n);

        // Find the nearest palindrome from candidates
        long closestPalindrome = -1;
        foreach (long candidate in candidates) {
            if (candidate == originalNumber) continue;

            if (closestPalindrome == -1 || 
                Math.Abs(candidate - originalNumber) < Math.Abs(closestPalindrome - originalNumber) ||
                (Math.Abs(candidate - originalNumber) == Math.Abs(closestPalindrome - originalNumber) && candidate < closestPalindrome)) {
                closestPalindrome = candidate;
            }
        }

        return closestPalindrome.ToString();
    }

    private string createPalindrome(string prefix, bool isEven) {
        var sb = new StringBuilder(prefix);
        for (int i = prefix.Length - (isEven ? 1 : 2); i >= 0; i--) {
            sb.Append(prefix[i]);
        }
        return sb.ToString();
    }

    private bool IsPowerOfTen(string n) {
        return n[0] == '1' && n.Substring(1).All(c => c == '0');
    }
}
