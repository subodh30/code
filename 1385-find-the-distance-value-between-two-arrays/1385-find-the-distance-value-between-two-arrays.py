class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        n2=sorted(arr2)
        ans=0
        for a in arr1:
            i, j = 0, len(arr2)-1
            ex=False
            while i <= j:
                mid = (i+j)//2
                if abs(n2[mid] - a) <= d:
                    ex=True
                    break
                elif n2[mid] > a:
                    j = mid - 1
                else:
                    i = mid + 1
            if not ex:
                ans+=1
        return ans
            
        