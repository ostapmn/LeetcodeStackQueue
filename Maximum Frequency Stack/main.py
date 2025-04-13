"""Maximum Frequency Stack"""


from collections import deque, defaultdict

class FreqStack:

    def __init__(self):
        self.stack = deque()


    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> int:
        max_freq = (0, None)
        used = set()
        for _ in range(len(self.stack)):
            x = self.stack.pop()
            self.stack.appendleft(x)
            if x not in used:
                used.add(x)
                if self.stack.count(x) > max_freq[0]:
                    max_freq = (self.stack.count(x), x)

        res = max_freq[1]
        for _ in range(len(self.stack)):
            x = self.stack.pop()
            if x == max_freq[1]:
                max_freq = (0, None)
            else:
                self.stack.appendleft(x)
        return res



freqStack = FreqStack()
freqStack.push(1)
freqStack.push(0)
freqStack.push(0)
freqStack.push(1)
freqStack.push(5)
freqStack.push(4)
freqStack.push(1)
freqStack.push(5)
freqStack.push(1)
freqStack.push(6)
print(freqStack.stack)
print(freqStack.pop())
print(freqStack.stack)
print(freqStack.pop())
print(freqStack.stack)
print(freqStack.pop())
print(freqStack.stack)
print(freqStack.pop())
print(freqStack.stack)
print(freqStack.pop())
print(freqStack.stack)
