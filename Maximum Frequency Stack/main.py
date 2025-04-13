"""Maximum Frequency Stack"""


from collections import deque, defaultdict

class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.mx = 0
        self.values = defaultdict(deque)


    def push(self, val: int) -> None:
        self.freq[val] += 1
        if self.freq[val]>=self.mx:
            self.mx = self.freq[val]
        self.values[self.freq[val]].append(val)

    def pop(self) -> int:
        if len(self.values[self.mx])==0:
            self.mx -= 1
        x = self.values[self.mx].pop()
        self.freq[x] = -1
        return x



freqStack = FreqStack()
freqStack.push(4)
freqStack.push(0)
freqStack.push(9)
freqStack.push(3)
freqStack.push(4)
freqStack.push(2)
print(freqStack.freq)
print(freqStack.values)
print(freqStack.pop())
print(freqStack.values)
print(freqStack.freq)
# freqStack.push(6)
# print(freqStack.pop())
# freqStack.push(1)
# print(freqStack.pop())
# freqStack.push(1)
# print(freqStack.values)
# print(freqStack.mx)
# print(freqStack.pop())
# freqStack.push(4)
# print(freqStack.pop())
# print(freqStack.pop())
# print(freqStack.pop())
# print(freqStack.pop())
# print(freqStack.pop())
# print(freqStack.pop())
