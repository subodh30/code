class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        
        while l < r :
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid +1
            else:
                r = mid
            
        rot = r
        
        l, r = 0, len(nums)-1
        
        while l <= r:
            mid = (l+r)//2
            mm = (mid+rot)%len(nums)
            if nums[mm]==target:
                return mm
            elif nums[mm] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
        