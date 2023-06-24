class NumArray:

    def __init__(self, nums: List[int]):
        self.bit = [0]*(len(nums) + 1)
        self.n = nums
        idx=1
        for x in nums:
            self.createBIT(idx, x)
            idx+=1
    
    def createBIT(self, idx, val):
        while idx < len(self.bit):
            self.bit[idx] += val
            idx += idx & (-idx)
        
    def update(self, index: int, val: int) -> None:
        d = val - self.n[index]
        self.n[index] = val
        index+=1
        while index < len(self.bit):
            self.bit[index]+=d
            index += index & (-index)
        
    def getSum(self, idx: int):
        s=0
        while idx > 0:
            s+=self.bit[idx]
            idx -= idx & (-idx)
        return s
    
    def sumRange(self, left: int, right: int) -> int:
        return self.getSum(right+1) - self.getSum(left) 
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)