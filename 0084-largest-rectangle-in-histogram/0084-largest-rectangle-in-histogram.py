class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        start=[]
        height=[]
        cur = 0
        ans = 0
        while cur < len(heights):
            if height:
                h, s = heights[cur], cur
                while height and heights[cur] < height[-1]:
                    h, s = height.pop(), start.pop()
                    ans = max(ans, (cur - s)*h)
                start.append(s)
                height.append(heights[cur])
            else:
                height.append(heights[cur])
                start.append(cur)
            cur+=1
        
        if height:
            while height:
                h, s = height.pop(), start.pop()
                ans = max(ans, (cur - s)*h)  
        return ans
                    