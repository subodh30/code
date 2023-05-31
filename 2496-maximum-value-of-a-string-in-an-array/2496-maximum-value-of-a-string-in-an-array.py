class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        mm=-1
        for i in strs:
            if i.isdigit():
                if mm < int(i):
                    mm = int(i)
            elif mm < len(i):
                mm = len(i)
                        
        return mm
        