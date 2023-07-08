class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if len(digits)==0:
            return []
        ans=[]
        def rec(idx, sidx, st):
            nonlocal d
            if idx == len(digits):
                ans.append(st)
                return 
            
            temp = d[digits[idx]]
            i = sidx
            while i < len(temp):
                rec(idx+1, sidx, st+temp[i])
                i+=1
                
        rec(0, 0, "")
        return ans
        