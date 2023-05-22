class MyQueue:

    def __init__(self):
        self.pust=[]
        self.post=[]
        

    def push(self, x: int) -> None:
        self.pust.append(x)
        

    def pop(self) -> int:
        if self.post:
            return self.post.pop()
        else:
            while self.pust:
                self.post.append(self.pust.pop())
        return self.post.pop()

    def peek(self) -> int:
        if self.post:
            return self.post[-1]
        else:
            while self.pust:
                self.post.append(self.pust.pop())
        return self.post[-1]
        

    def empty(self) -> bool:
        return len(self.pust)==0 and len(self.post)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()