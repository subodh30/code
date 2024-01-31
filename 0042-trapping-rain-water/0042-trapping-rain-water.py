class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        maxL = [0 for _ in range(len(height))]
        maxL[1] = max(height[0], maxL[0])
        for i in range(2, len(height)):
            maxL[i] = max(maxL[i-1], height[i-1])
        height = height[::-1]
        maxR = [0 for _ in range(len(height))]
        maxR[1] = max(height[0], maxR[0])
        for i in range(2, len(height)):
            maxR[i] = max(maxR[i-1], height[i-1])
        maxR = maxR[::-1]
        height = height[::-1]

        ans = 0
        for i, h in enumerate(height):
            ans += max(0, min(maxL[i], maxR[i]) - h)
            
        return ans
                
                