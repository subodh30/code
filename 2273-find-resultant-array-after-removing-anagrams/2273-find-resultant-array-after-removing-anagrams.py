class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans=[]
        ans.append(words[0])
        for i in range(1, len(words)):
            if sorted(words[i-1]) == sorted(words[i]):
                if sorted(ans[-1])!=sorted(words[i-1]):
                    ans.append(words[i-1])
            else:
                ans.append(words[i])
                
        return ans
        