class Solution:
    def checkValidString(self, s: str) -> bool:
        openMin, openMax = 0,0
        for i in s:
            if i == '(':
                openMin, openMax = openMin + 1, openMax + 1
            elif i == ')':
                openMin, openMax = max(openMin-1, 0), openMax - 1
            else:
                openMin, openMax = max(openMin - 1, 0), openMax + 1
            if openMax < 0:
                return  False
        return openMin == 0
            
        
        