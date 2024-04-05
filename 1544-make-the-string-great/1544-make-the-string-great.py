class Solution:
    def makeGood(self, s: str) -> str:
        st=[]
        for i in s:
            if len(st)!=0 and st[-1].lower() == i.lower() and st[-1]!=i:
                st.pop()
            else:
                st.append(i)
        return ''.join(st)
        