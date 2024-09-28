"""
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.

A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendarTwo class:

    MyCalendarTwo() Initializes the calendar object.
    boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
"""
class MyCalendarTwo(object):

    def __init__(self):
        self.events = {}

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        # Initialize keys if they don't exist
        if start not in self.events:
            self.events[start] = 0
        if end not in self.events:
            self.events[end] = 0

        self.events[start] += 1
        self.events[end] -= 1

        ongoingEvents = 0

        # Check for ongoing events to see if we reach triple booking
        for event in sorted(self.events.keys()):
            ongoingEvents += self.events[event]
            
            # Undo the changes if triple booking occurs
            if ongoingEvents >= 3:
                self.events[start] -= 1
                self.events[end] += 1
                return False
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
