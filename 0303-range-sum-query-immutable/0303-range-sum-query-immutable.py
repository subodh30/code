class NumArray:

    def __init__(self, nums: List[int]):
        self.n = nums
        self.l = []
        self.r =[]
        tsum=0
        for x in self.n:
            self.l.append(tsum)
            tsum+=x
        tsum=0
        rt=[]
        for x in self.n[::-1]:
            rt.append(tsum)
            tsum+=x
        self.r = rt[::-1]
        self.tot = sum(nums)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.tot - self.r[right] - self.l[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)