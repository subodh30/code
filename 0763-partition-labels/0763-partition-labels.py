class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #ord 97-a 65-A 48-1
        cnt = [0 for _ in range(26)]
        for i in s:
            cnt[ord(i)-97] += 1
        
        chrset = set()
        ans = []
        start = 0
        for i, v in enumerate(s):
            chrset.add(v)
            cnt[ord(v)-97] -= 1
            if cnt[ord(v)-97] == 0:
                chrset.remove(v)
                
            if len(chrset) == 0:
                ans.append(i+1 - start)
                start = i + 1
        return ans