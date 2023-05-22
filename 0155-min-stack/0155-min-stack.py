class MinStack:

    def __init__(self):
        self.st=[]
        self.minst=[]
        

    def push(self, val: int) -> None:
        self.st.append(val)
        print(self.minst)
        if len(self.minst)==0 or self.minst[-1][0] > val:
            self.minst.append([val, len(self.st)])

    def pop(self) -> None:
        ele = self.st.pop()
        if self.minst[-1][1] > len(self.st):
            self.minst.pop()
        

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.minst[-1][0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()