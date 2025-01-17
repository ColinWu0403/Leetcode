"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.
"""
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """

        intervals.sort(key=lambda x: x[0])
        result = 0
        previnter = intervals[0][1]

        for i in range(1, len(intervals)):
            if previnter > intervals[i][0]:
                result += 1
                previnter = min(intervals[i][1], previnter)
            else:
                previnter = intervals[i][1]
        return result
