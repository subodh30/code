class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1
        def getDiff(g1, g2):
            ans = 0
            for i in range(len(g1)):
                if g1[i] == g2[i]:
                    continue
                ans += 1
            return ans
                
        def dfs(curGene, visited):
            # print(curGene)
            if curGene == endGene:
                return 0
            
            ans = float("inf")
            for x in bank:
                if x not in visited and getDiff(x, curGene) == 1:
                    visited.add(x)
                    ans = min(ans, 1 + dfs(x, visited))
                    visited.remove(x)
            return ans
                    
                    
                    
        vis = set()
        
        ret = dfs(startGene, vis)
        
        return -1 if ret == float("inf") else ret
        