class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def rec(val, oc, cc, n, ans):
            
            def valid(s):
                st=[]
                for i in s:
                    if i == "(":
                        st.append(")")
                    else:
                        if len(st)==0:
                            return False
                        st.pop()
                return len(st)==0
            
            if oc==n and cc==n:
                if valid(val):
                    ans.append(val)
                return
            
            if oc < n:
                rec(val+"(", oc+1, cc, n, ans)
            
            if cc < n:
                rec(val+")", oc, cc+1,n, ans)
            
            return
        
        ans =[]
        rec("", 0, 0, n, ans)
        return ans
                