class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        q = collections.deque()
        i=0
        while i < k:
            while  q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])
            i=i+1
            
        l, r = 0, k
        while r < len(nums):
            res.append(q[0])
            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])
            
            if nums[l] == q[0]:
                q.popleft()
            l+=1
            r+=1
        res.append(q[0])
        return res
        
            
            
        