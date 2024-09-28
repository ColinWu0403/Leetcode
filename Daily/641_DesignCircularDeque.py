"""
Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

    MyCircularDeque(int k) Initializes the deque with a maximum size of k.
    boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
    boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
    boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
    boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
    int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
    int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
    boolean isEmpty() Returns true if the deque is empty, or false otherwise.
    boolean isFull() Returns true if the deque is full, or false otherwise.
"""
class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        :fields:
        :cirdq = list representing circular deque
        :front = front pointer
        :back = back pointer
        :size = current size of deque
        :capacity = max size of deque
        """
        self.cirdq = [-1] * k
        self.front = 0
        self.back = 0
        self.size = 0
        self.capacity = k

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        
        if self.front == 0:
            self.front = self.capacity - 1 # move to back since it is circular
        else:
            self.front -= 1

        self.cirdq[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        
        self.cirdq[self.back] = value

        if self.back == self.capacity - 1:
            self.back = 0 # move to front since it is circular
        else:
            self.back += 1
        
        self.size += 1
        return True

    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False

        self.cirdq[self.front] = -1

        if self.front == self.capacity - 1:
            self.front = 0 # move to beginning
        else:
            self.front += 1

        self.size -= 1
        return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False

        if self.back == 0:
            self.back = self.capacity - 1 # move to back
        else:
            self.back -= 1

        self.cirdq[self.back] = -1
        self.size -= 1
        return True

    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.cirdq[self.front]

    def getRear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        if self.back == 0:
            return self.cirdq[self.capacity - 1]
        else:
            return self.cirdq[self.back - 1]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.size == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
