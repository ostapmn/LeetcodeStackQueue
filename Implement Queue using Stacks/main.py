"""Implement Queue using Stacks"""


class MyStack:
    """Stack data structure"""
    def __init__(self):
        """Class initializer"""
        self.__container = []

    def size(self):
        return len(self.__container)

    def is_empty(self):
        return self.size() == 0

    def push(self, value):
        self.__container.append(value)

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.__container[-1]

    def pop(self):
        return self.__container.pop()



class MyQueue:
    """Queue Data Structure"""
    def __init__(self):
        """Class initializer"""
        self.all_info = MyStack()
        self.trash = MyStack()
        self.size = 0

    def push(self, x: int) -> None:
        self.all_info.push(x)
        self.size += 1

    def pop(self) -> int:
        if self.empty():
            return "Queue has ended"
        if not self.all_info.is_empty() and self.trash.is_empty(): # last element you get from stack
            for _ in range(self.all_info.size()):                  # it's the first you get from queue
                self.trash.push(self.all_info.pop())               # sosecond stack it's the reversed first stack
        self.size -= 1
        return self.trash.pop()


    def peek(self) -> int:
        if self.empty():
            return "Queue has ended"
        if not self.all_info.is_empty() and self.trash.is_empty():
            for _ in range(self.all_info.size()):
                self.trash.push(self.all_info.pop())
        return self.trash.peek()

    def empty(self) -> bool:
        return self.size == 0




# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()