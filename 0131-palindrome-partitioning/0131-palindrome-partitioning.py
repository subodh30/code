class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPal(st):
            i,j = 0, len(st)-1
            while i<j:
                if st[i]==st[j]:
                    i+=1
                    j-=1
                else:
                    return False
            return True
        
        ans=[]
        
        def rec(idx, arr):
            nonlocal ans
            if idx==len(s):
                ans.append(arr.copy())
                return
            i=idx+1
            while i <= len(s):
                if isPal(s[idx:i]):
                    arr.append(s[idx:i])
                    rec(i, arr)
                    arr.pop()
                i+=1
        rec(0, [])
        return ans
        