class Solution:
    def searchMatrix(self, m: List[List[int]], target: int) -> bool:
        l,r = 0, len(m)-1
        
        row = -1
        while l <=r:
            mid = (l+r)//2
            if m[mid][0] == target:
                return True
            elif target < m[mid][0]:
                r = mid - 1
            else: 
                l = mid + 1
                
        row = r
        l, r = 0, len(m[0]) -1 
        while l <= r:
            mid = (l+r)//2
            if m[row][mid]==target:
                return True
            elif target < m[row][mid]:
                r = mid -1
            else: 
                l = mid +1
        return False
            
            
        
        
