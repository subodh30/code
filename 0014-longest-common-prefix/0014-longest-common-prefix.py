class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        ans = ""
        comp = strs[0]
        i = 1
        while i < len(strs):
            l, m = 0, 0
            ans = ""
            while l < len(comp) and m < len(strs[i]) and comp[l] == strs[i][m]:
                ans+=comp[l]
                l+=1
                m+=1
            
            if ans == "":
                return ""
            
            comp = ans
            i+=1
        
        return ans