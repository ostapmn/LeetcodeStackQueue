"""Maximum Frequency Stack"""


from collections import deque, defaultdict

class FreqStack:

    def __init__(self):
        self.stack = deque()
        self.trash = deque()
        self.values = defaultdict(int)

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.values[val]+=1

    def pop(self) -> int:
        max_freq = (0, None)
        # for _ in range(len(self.stack)):
        #     x = self.stack.popleft()
        #     self.stack.append(x)
        #     if self.stack.count(x) >= max_freq[0]:
        #         max_freq = (self.stack.count(x), x)
        for el in self.stack:
            if self.stack.count(el) >= max_freq[0]:
                max_freq = (self.stack.count(el), el)
        res = max_freq[1]
        for _ in range(len(self.stack)):
            x = self.stack.pop()
            if x == max_freq[1]:
                max_freq = (0, None)
            else:
                self.stack.appendleft(x)
        return res



freqStack = FreqStack()
freqStack.push(5)
freqStack.push(7)
freqStack.push(5)
freqStack.push(7)
freqStack.push(4)
freqStack.push(5)
print(freqStack.pop())
print(freqStack.stack)
print(freqStack.pop())
print(freqStack.stack)
print(freqStack.pop())
print(freqStack.stack)
print(freqStack.pop())
print(freqStack.stack)
# for el in freqStack.stack:
#     print(el, end = ' ')
#ject will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()