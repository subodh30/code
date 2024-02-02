class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st =[]
        for x in tokens:
            if x == "+":
                st.append(st.pop() + st.pop())
                continue
            if x == "-":
                b = st.pop()
                a = st.pop()
                st.append(a - b)
                continue
            if x == "*":
                st.append(st.pop() * st.pop())
                continue
            if x == "/":
                b = st.pop()
                a = st.pop()
                ans = a / b
                if ans < 0:
                    ans = math.ceil(ans)
                else:
                    ans = math.floor(ans)
                st.append(ans)
                continue
            st.append(int(x))
            
        return st[-1]
                