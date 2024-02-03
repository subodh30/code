class Solution:
    def searchMatrix(self, m: List[List[int]], target: int) -> bool:
        l, r = 0, len(m)-1
        row = -1
        while l <= r:
            mid = (l+r)//2
            if m[mid][0] < target:
                l = mid+1
            elif m[mid][0] > target:
                r = mid - 1
            else:
                return True
        row = r
        l, r = 0, len(m[0]) - 1
        while l <= r:
            mid = (l+r)//2
            if m[row][mid] < target:
                l=mid+1
            elif m[row][mid] > target:
                r = mid -1
            else:
                return True
        return False
            
        
        
