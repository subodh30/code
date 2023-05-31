class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans=set()
        r=[]
        for i in range(0, len(nums)):
            if nums[i] == key:
                r.append(i)
        for i in r:
            ans.add(i)
            x=i-1
            
            while x!=-1 and k >= abs(i-x):
                # print(str(abs(i-x)) + " " + str(x))
                ans.add(x)
                x-=1
            # print("\n")
            x = i+1
            while x!=len(nums) and k >= abs(i-x):
                # print(str(abs(i-x)) + " " + str(x))
                ans.add(x)
                x+=1
        
        return list(ans)