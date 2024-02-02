class MinStack:

    def __init__(self):
        self.st = []
        self.minst = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if self.minst:
            self.minst.append(min(self.minst[-1], val))
        else:
            self.minst.append(val)
        

    def pop(self) -> None:
        self.st.pop()
        self.minst.pop()
        

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.minst[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()