"""
Design a stack that supports increment operations on its elements.

Implement the CustomStack class:

    CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
    void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
    int pop() Pops and returns the top of the stack or -1 if the stack is empty.
    void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, increment all the elements in the stack.
"""
class CustomStack(object):
  
    # use another stack incVals to delay increments of the value to when we need to push and pop, this acheives O(1) amoritzed time
    def __init__(self, maxSize):
        """
        :type maxSize: int
        """
        self.stack = []
        self.incVals = [0] * maxSize
        self.maxSize = maxSize

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if (len(self.stack) < self.maxSize):
            self.stack.append(x)
        else:
            self.incVals.append(0)

    def pop(self):
        """
        :rtype: int
        """
        if not self.stack:
            return -1

        # Apply any deferred increment to the top of the stack
        idx = len(self.stack) - 1
        poppedVal = self.stack.pop() + self.incVals[idx]
        
        # Pass the increment value to the next element (if any)
        if idx > 0:
            self.incVals[idx - 1] += self.incVals[idx]
        
        self.incVals[idx] = 0
        
        return poppedVal
    
    def increment(self, k, val):
        """
        :type k: int
        :type val: int
        :rtype: None
        """
        # Increment the first `k` elements (or all if `k > len(self.stack)`)
        limit = min(k, len(self.stack)) - 1
        if limit >= 0:
            self.incVals[limit] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
