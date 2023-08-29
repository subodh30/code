class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        larr=[]
        tot = 0
        for x in nums:
            larr.append(tot)
            tot+=x
            
        rarr=[]
        tot=0
        for x in nums[::-1]:
            rarr.append(tot)
            tot+=x
        rarr = rarr[::-1]
        # print(larr)
        # print(rarr)
        i=0
        while i < len(nums):
            if larr[i] == rarr[i]:
                return i
            i+=1
        return -1