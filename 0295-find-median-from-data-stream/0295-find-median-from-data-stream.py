class MedianFinder:

    def __init__(self):
        self.nums=[]
        self.n=0
        

    def addNum(self, num: int) -> None:
        
        if self.nums and num <= self.nums[0]:
            self.nums.insert(0, num)
            self.n+=1
            return
    
        if self.nums and num >= self.nums[self.n-1]:
            self.nums.insert(self.n, num)
            self.n+=1
            return
        i, j = 0, self.n - 1
        pos = None
        while i <= j:
            mid = (i+j)//2
            if self.nums[mid]  == num:
                pos=mid
                break
            elif self.nums[mid] > num:
                j = mid - 1
            else:
                i = mid + 1
        if pos == None:
            self.nums.insert(i, num)
            self.n+=1
            return
        self.nums.insert(pos, num)
        self.n+=1
        return
        

    def findMedian(self) -> float:
        if self.n%2:
            return self.nums[self.n//2]
        
        l,k = self.n//2, self.n//2 - 1
        return (self.nums[l] + self.nums[k]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()