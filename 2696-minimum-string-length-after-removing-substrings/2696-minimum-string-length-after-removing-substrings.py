class Solution:
    def minLength(self, s: str) -> int:
        st=[]
        for i in s:
            if i == "D" and st and st[-1]=="C":
                    st.pop()
            elif i=="B" and st and st[-1]=="A":
                    st.pop()
            else:
                st.append(i)
        return len(st)