class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        st=[]
        for i in s:
            if i=="(":
                st.append("(")
            
            if i==")":
                ans = max(ans, len(st))
                st.pop()
        return ans
        