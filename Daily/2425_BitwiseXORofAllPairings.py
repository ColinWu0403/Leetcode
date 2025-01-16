"""
You are given two 0-indexed arrays, nums1 and nums2, consisting of non-negative integers. There exists another array, nums3, which contains the bitwise XOR of all pairings of integers between nums1 and nums2 (every integer in nums1 is paired with every integer in nums2 exactly once).

Return the bitwise XOR of all integers in nums3.
"""
class Solution(object):
    def xorAllNums(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        xor1 = 0
        xor2 = 0

        for num in nums1:
            xor1 ^= num
        
        for num in nums2:
            xor2 ^= num

        # Use greedy approach since a number XOR itself is 0
        if len(nums2) % 2 == 0:
            if len(nums1) % 2 != 0:
                return xor2
            else:
                return 0
        else:
            if len(nums1) % 2 == 0:
                return xor1
            else:
                return xor1 ^ xor2
