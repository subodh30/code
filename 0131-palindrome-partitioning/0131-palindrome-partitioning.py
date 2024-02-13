class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def isPal(ss):
            half=len(ss)//2
            fir = ss[:half]
            sec = ss[half if len(ss)%2==0 else half+1:]
            sr = sec[::-1]
            return fir == sr
        
        def test(i, temp):
            if i >= len(s):
                ans.append(temp.copy())
                return
            # print(i)
            for xi in range(i, len(s)+1):
                # print(s[i:xi])
                if s[i:xi] != "" and isPal(s[i:xi]):
                    temp.append(s[i:xi])
                    test(xi, temp)
                    temp.pop()
        test(0, [])
        return ans