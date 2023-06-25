class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        st = []
        lc=[]
        h.append(0)
        maxArea = 0
        for i, x in enumerate(h):
            if len(st)== 0 or st[-1] <= x:
                st.append(x)
                lc.append(i)
            else:
                l = i
                while st and st[-1] > x:
                    s = st.pop()
                    l = lc.pop()
                    maxArea = max(maxArea, (i-l)*s)
                st.append(x)
                lc.append(l)
        return maxArea