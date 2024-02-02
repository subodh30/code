class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        st = []
        ans = []
        for i in range(len(t)-1, -1, -1):
            if not st:
                ans.append(0)
            else:
                while st and t[st[-1]] <= t[i]:
                    st.pop()
                if st:
                    ans.append(st[-1] - i)
                else:
                    ans.append(0)
            st.append(i)
        return ans[::-1]
                