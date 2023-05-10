class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        sdir = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss not in sdir:
                sdir[ss] = []
            sdir[ss].append(s)
            
        for s in sdir.values():
            ans.append(s)
        return ans
        