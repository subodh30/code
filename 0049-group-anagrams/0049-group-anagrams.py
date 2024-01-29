class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for st in strs:
            srt = sorted(st)
            srt = ''.join(srt)
            if d.get(srt, None) == None:
                d[srt] = []
            d[srt].append(st)
            
        ans = []
        for v in d.values():
            ans.append(v)
            
        return ans