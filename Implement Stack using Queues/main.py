"""Implement Stack using Queues"""

class MyQueue:
    """Queu data structure"""

    def __init__(self):
        self.__container = []


    def size(self):
        return len(self.__container)


    def is_empty(self):
        return self.size() == 0


    def push(self, val):
        self.__container.append(val)


    def pop(self):
        if self.size() == 0:
            return "Queue has ended"
        return self.__container.pop(0)


    def peek(self):
        if self.size() == 0:
            return "Queue has ended"
        return self.__container[0]

class MyStack:

    def __init__(self):
        self.main = MyQueue()
        self.trash = MyQueue()
        self.size = 0

    def push(self, x: int) -> None:
        self.main.push(x)
        self.size += 1

    def pop(self) -> int:
        self.size -= 1                            # last element in queue become first to
        if self.main.size() == 0:                 # out if it's the last element
            for _ in range(self.trash.size()):
                self.main.push(self.trash.pop())
        if self.main.size() == 1:
            return self.main.pop()
        for _ in range(self.main.size()-1):
            self.trash.push(self.main.pop())
        return self.main.pop()


    def top(self) -> int:
        if self.main.size() == 0:
            for _ in range(self.trash.size()):
                self.main.push(self.trash.pop())
        if self.main.size() == 1:
            return self.main.peek()
        for _ in range(self.main.size()-1):
            self.trash.push(self.main.pop())
        return self.main.peek()

    def empty(self) -> bool:
        return self.size == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

