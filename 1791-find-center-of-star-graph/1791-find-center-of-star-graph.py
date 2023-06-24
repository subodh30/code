class Solution:
    def findCenter(self, e: List[List[int]]) -> int:
        if e[0][0] in e[1]:
            return e[0][0]
        
        return e[0][1]
        