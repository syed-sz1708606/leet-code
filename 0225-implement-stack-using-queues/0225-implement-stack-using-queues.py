import collections
class MyStack(object):

    def __init__(self):
        self._queue = collections.deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        return self._queue.appendleft(x)

    def pop(self):
        """
        :rtype: int
        """
        return self._queue.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self._queue[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self._queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()