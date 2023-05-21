class Solution:
    def minOperations(self, logs: List[str]) -> int:
        st=[]
        for i in logs:
            if i=="../":
                if st:
                    st.pop()
            elif i=="./":
                pass
            else:
                st.append(i)
        return len(st)
        