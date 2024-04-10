class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        
        #print(s)
        def getSum(idx):
            i = idx
            st, num, neg = [], 0, False
            while i < len(s) and s[i] != ")":
                #print("i"+ str(i))
                #print(st)
                if s[i].isnumeric():
                    num *= 10
                    num += int(s[i])
                elif s[i] == "+":
                    st.append(-num if neg else num)
                    num, neg = 0, False
                elif s[i] == "-":
                    st.append(-num if neg else num)
                    num, neg = 0, True
                elif s[i] == "(":
                    sx, i = getSum(i+1)
                    st.append(-sx if neg else sx)
                i+=1
            st.append(-num if neg else num)
            return sum(st), i
        return getSum(0)[0]
        
            
            