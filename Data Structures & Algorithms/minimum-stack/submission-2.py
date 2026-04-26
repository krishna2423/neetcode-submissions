class MinStack:

    def __init__(self):
        self.stack = []
        self.minimums = []

    def push(self, val: int) -> None:
        if not self.minimums:
            self.minimums.append(val)
        elif val <= self.minimums[-1]:
            self.minimums.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        elem = self.stack.pop()
        if elem == self.minimums[-1]:
            self.minimums.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minimums:
            return self.minimums[-1]
