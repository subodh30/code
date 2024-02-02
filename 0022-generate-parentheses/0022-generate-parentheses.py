class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret=set()
        st=["("]
        def valid(st):
            t=[]
            for x in st:
                if x == "(":
                    t.append(x)
                if x == ")":
                    if t and t[-1] == "(":
                        t.pop()
                    else:
                        return False
            return False if t else True
            
            
        def check():
            if len(st) == (2*n):
                if valid(st):
                    print(st)
                    ret.add("".join(st))
                return
                  
            st.append("(")
            check()
            st.pop()
            st.append(")")
            check()
            st.pop()
            return 
        
        check()
        return ret
            